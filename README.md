# rustfuture

Rust backend, systems programming, and applied LLM experiments.

This profile is a small, evidence-led portfolio. Public repositories focus on tools that can be inspected, built, and tested from their own documentation. Private research projects are described only at a high level until they are ready to be reviewed publicly.

## Public projects

| Project | What you can inspect | Main engineering themes |
| --- | --- | --- |
| [grainx](https://github.com/rustfuture/grainx) | A terminal system monitor with local CPU, memory, disk, network, process, and host information; an optional HTTP metrics service; and JSON/CSV export. | Rust systems programming, terminal UI, telemetry, and a small HTTP service. |
| [deltasafe](https://github.com/rustfuture/deltasafe) | An authenticated directory-transfer prototype for a trusted LAN, with encrypted bounded frames, integrity verification, and non-overwrite file publication. | Protocol design, cryptographic boundaries, streaming I/O, and failure handling. |
| [RustHound](https://github.com/rustfuture/RustHound) | A streaming log-analysis CLI with configurable string, regular-expression, frequency, and correlation rules plus console and JSON output. | Parsing, rule evaluation, CLI design, and incremental analysis. |

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
