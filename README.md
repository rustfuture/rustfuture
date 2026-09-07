# Özgür

**Rust Backend · Systems Programming · Applied LLM**

I build Rust tools for monitoring systems, transferring files, and working with data. I'm also developing LLM-assisted developer tools, with a focus on controlled execution and evaluating whether their outputs are actually useful.

## Selected work

| Project | What it does | Engineering focus |
| :--- | :--- | :--- |
| **[grainx](https://github.com/rustfuture/grainx)** | Terminal system monitor with an HTTP metrics service and JSON/CSV export. | System telemetry, terminal interfaces, and local/remote operation. |
| **[deltasafe](https://github.com/rustfuture/deltasafe)** | Authenticated directory-to-directory file transfer over a trusted LAN. | Bounded protocol frames, integrity checks, and publishing only verified files. |
| **[RustHound](https://github.com/rustfuture/RustHound)** | Command-line log analysis using configurable detection rules. | Streaming input, pattern matching, and frequency/correlation rules. |

### A closer look

- **grainx:** [Run the dashboard](https://github.com/rustfuture/grainx#quick-start) or explore the [module architecture](https://github.com/rustfuture/grainx/blob/main/docs/architecture.md).
- **deltasafe:** Follow an [end-to-end transfer](https://github.com/rustfuture/deltasafe#usage) and read the [protocol's security boundaries](https://github.com/rustfuture/deltasafe#security-boundaries).
- **RustHound:** Try the [sample log and rules](https://github.com/rustfuture/RustHound#quick-start).

## In progress: applied LLM

Alongside my public Rust projects, I'm working on three private experiments:

- **Agent runtime** — persistent task state, bounded tool execution, and explicit verification after code edits.
- **Repository intelligence** — lexical code retrieval, incremental indexing, and source-referenced model answers.
- **Model adaptation lab** — local LoRA experiments on synthetic Rust-error examples, comparing base-model and adapter outputs.

These are development-stage projects, not public releases. The model-adaptation work currently documents a negative result rather than a demonstrated quality improvement.

---

For setup instructions, tests, design decisions, and current limitations, start with the individual project READMEs.
