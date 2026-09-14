# rustfuture

Rust backend, systems programming, and applied LLM experiments.

This profile is a small, evidence-led portfolio. Public repositories focus on tools that can be inspected, built, and tested from their own documentation. Private research projects are described only at a high level until they are ready to be reviewed publicly.

## Public projects

Each project builds from a committed lockfile, runs its own test suite, is checked by GitHub Actions
on every push to `main`, and has a tagged release you can check out.

| Project | CI | Release | Tests | What you can inspect |
| --- | --- | --- | --- | --- |
| [grainx](https://github.com/rustfuture/grainx) | [![grainx CI](https://github.com/rustfuture/grainx/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/rustfuture/grainx/actions/workflows/ci.yml) | [v0.1.0](https://github.com/rustfuture/grainx/releases/tag/v0.1.0) | 82 passing | A terminal system monitor with local CPU, memory, disk, network, process, and host information; an optional HTTP metrics service; and JSON/CSV export. |
| [deltasafe](https://github.com/rustfuture/deltasafe) | [![deltasafe CI](https://github.com/rustfuture/deltasafe/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/rustfuture/deltasafe/actions/workflows/ci.yml) | [v0.1.0](https://github.com/rustfuture/deltasafe/releases/tag/v0.1.0) | 30 passing | An authenticated directory-transfer tool for a trusted LAN, with encrypted bounded frames, integrity verification, and non-overwrite file publication. |
| [RustHound](https://github.com/rustfuture/RustHound) | [![RustHound CI](https://github.com/rustfuture/RustHound/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/rustfuture/RustHound/actions/workflows/ci.yml) | [v0.1.0](https://github.com/rustfuture/RustHound/releases/tag/v0.1.0) | 12 passing | A streaming log-analysis CLI with configurable string, regular-expression, frequency, and correlation rules plus console and JSON output. |

Each project states its own versioning policy: while the major version is `0`, the version number
describes scope rather than a compatibility promise, and a breaking change bumps the minor version.

Local reproduction for any project follows the same shape:

```bash
cargo fmt --check
cargo clippy --locked --all-targets -- -D warnings
cargo test --locked
```

deltasafe's suite is serialized, because its loopback tests bind ephemeral ports and share process
state; use the invocation its own README and CI use:

```bash
cargo test --locked -- --test-threads=1
```

## Where to start

- [grainx quick start](https://github.com/rustfuture/grainx#quick-start) · [architecture](https://github.com/rustfuture/grainx/blob/main/docs/architecture.md)
- [deltasafe usage](https://github.com/rustfuture/deltasafe#usage) · [security boundaries](https://github.com/rustfuture/deltasafe#security-boundaries)
- [RustHound quick start](https://github.com/rustfuture/RustHound#quick-start)

Each project README contains the supported setup, test commands, design notes, and known limitations. The projects are prototypes rather than claims of universal production readiness: for example, grainx's optional HTTP service is not an authenticated internet-facing service, and deltasafe is designed around a trusted-LAN boundary.

## Private applied-LLM work

The following work remains private and is not presented as a public release:

- **Agent runtime:** persistent task state, bounded subprocess/tool execution, structured model calls, and explicit verification after edits.
- **Repository intelligence:** lexical code retrieval, incremental indexing, provider boundaries, and source-linked answers.
- **Model adaptation lab:** local LoRA experiments on synthetic Rust-error data with a held-out evaluation. Current results are recorded as experimental, including cases where adaptation did not improve the baseline.

## Working principles

- Prefer reproducible commands and measured behavior over broad claims.
- Document security, access, and deployment boundaries next to the feature they qualify.
- Keep prototypes small enough to inspect, test, and explain.
