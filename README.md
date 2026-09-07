# Özgür — Rust backend & systems

I build command-line tools and backend services in Rust. My current work explores system monitoring, authenticated file transfer, and how to test the boundaries of LLM-assisted developer tools.

## Public projects

### [grainx](https://github.com/rustfuture/grainx)

A terminal system monitor with an optional HTTP metrics process and JSON/CSV export. The repository covers local collection, remote metrics, configuration, and the limits of its current platform verification.

[Quick start](https://github.com/rustfuture/grainx#quick-start) · [Architecture](https://github.com/rustfuture/grainx/blob/main/docs/architecture.md)

### [deltasafe](https://github.com/rustfuture/deltasafe)

An authenticated file-transfer prototype for a trusted LAN. The receiver verifies encrypted frames, file size, and a BLAKE3 digest before publishing a file without overwriting an existing destination. Its documented threat model explains what the protocol does **not** protect against.

[Usage](https://github.com/rustfuture/deltasafe#usage) · [Security boundaries](https://github.com/rustfuture/deltasafe#security-boundaries)

### [RustHound](https://github.com/rustfuture/RustHound)

A smaller log-analysis CLI with configurable string, regex, frequency, and correlation rules. Includes a sample log and rules for a reproducible first run.

## Work in progress — private repositories

These projects are not currently available for public code review:

- **rust-agent-runtime:** persistent task state, bounded command execution, and explicit post-edit verification for a coding-agent prototype.
- **repository-intelligence:** lexical code search and experimental LLM answers. Snapshot consistency and answer grounding remain areas of development.
- **model-adaptation-lab:** a small local LoRA experiment on synthetic Rust-error examples. The recorded adapter did not improve held-out keyword coverage; this is a negative-result study, not a model-quality claim.
- **searchoptservice:** an embedded product-search backend using sled.

The public repositories are pre-1.0 projects. Their README files distinguish implemented behavior, tested scenarios, and remaining limitations.
