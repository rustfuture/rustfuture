"""Check profile links against public GitHub repository files and headings."""
import base64
import json
import os
from pathlib import Path
import re
from urllib.parse import quote, urlparse
from urllib.request import Request, urlopen

CACHE = {}

def api(path):
    if path not in CACHE:
        headers = {"Accept": "application/vnd.github+json", "User-Agent": "profile-link-check"}
        token = os.environ.get("GITHUB_TOKEN")
        if token:
            headers["Authorization"] = "Bearer " + token
        with urlopen(Request("https://api.github.com/" + path, headers=headers), timeout=30) as response:
            CACHE[path] = json.load(response)
    return CACHE[path]

def headings(text):
    anchors = set()
    seen = {}
    fenced = False
    for line in text.splitlines():
        if re.match(r"^\s*(?:`{3,}|~{3,})", line):
            fenced = not fenced
            continue
        match = re.match(r"^#{1,6}\s+(.+)$", line)
        if fenced or not match:
            continue
        heading = re.sub(r"<[^>]+>", "", match.group(1)).strip().lower()
        heading = re.sub(r"[`*~\[\]()]", "", heading)
        anchor = re.sub(r"[^\w\- ]", "", heading).replace(" ", "-")
        count = seen.get(anchor, 0)
        seen[anchor] = count + 1
        anchors.add(anchor if count == 0 else f"{anchor}-{count}")
    return anchors

def main():
    readme = Path(__file__).resolve().parents[1] / "README.md"
    text = readme.read_text(encoding="utf-8")
    urls = sorted(set(re.findall(r"\]\((https://[^)]+)\)", text)))
    if not urls:
        raise ValueError("README has no project links")
    repos = set()
    for url in urls:
        parsed = urlparse(url)
        parts = parsed.path.strip("/").split("/")
        if parsed.netloc != "github.com" or len(parts) < 2 or parts[0] != "rustfuture":
            raise ValueError(f"Unsupported profile link: {url}")
        repo = parts[1]
        repos.add(repo)
        base = "repos/rustfuture/" + quote(repo, safe="")
        if len(parts) == 2:
            api(base)
            path = "README.md"
        elif len(parts) >= 5 and parts[2:4] == ["blob", "main"]:
            path = "/".join(parts[4:])
            api(base + "/contents/" + quote(path, safe="/") + "?ref=main")
        else:
            raise ValueError(f"Unsupported project path: {url}")
        if parsed.fragment:
            content = api(base + "/contents/" + quote(path, safe="/") + "?ref=main")
            source = base64.b64decode(content["content"]).decode("utf-8")
            if parsed.fragment not in headings(source):
                raise ValueError(f"Missing heading: {url}")
        print("PASS", url)
    print(f"PASS: {len(urls)} links across {len(repos)} project repositories")

if __name__ == "__main__":
    main()
