# rustfuture

**Rust systems · Agent infrastructure · Applied LLM research**

*Reproducible experiments, explicit boundaries, measured behavior.*

![Rust](https://img.shields.io/badge/rust-1.85%2B-orange?style=flat-square)
![Python](https://img.shields.io/badge/python-3.9%2B-blue?style=flat-square)
![License: MIT](https://img.shields.io/badge/license-MIT-green?style=flat-square)

## Featured Research & Systems

### [Reflex Control](https://github.com/rustfuture/reflex-control)

Calibrated System-1 control plane and policy engine in Rust for AI agent runtimes. Couples zero-cost deterministic checks with atomic semantic signals from TypeSafe Jev to eliminate routine frontier calls (69% autonomous coverage) while enforcing inviolable hard safety vetoes against dangerous operations.

[README / Quick Start](https://github.com/rustfuture/reflex-control#quick-start) · [Architecture](https://github.com/rustfuture/reflex-control#workspace-architecture) · [Evaluation Benchmark](https://github.com/rustfuture/reflex-control#evaluation-benchmark--measured-results) · [Runnable Examples](https://github.com/rustfuture/reflex-control#runnable-examples)

### [Rust Agent Runtime](https://github.com/rustfuture/rust-agent-runtime)

Durable, bounded execution runtime for coding-agent experiments with explicit verification, crash-recoverable task state, and constrained tool authority.

[README / Quick Start](https://github.com/rustfuture/rust-agent-runtime#quick-start) · [Architecture](https://github.com/rustfuture/rust-agent-runtime/blob/main/docs/architecture.md) · [Evaluation Evidence](https://github.com/rustfuture/rust-agent-runtime#evaluation-evidence)

### [Repository Intelligence](https://github.com/rustfuture/repository-intelligence)

Evidence-first repository retrieval in Rust with lexical, vector, and hybrid search plus extractive source selection and bounded context assembly.

[Architecture](https://github.com/rustfuture/repository-intelligence#architecture) · [Results](https://github.com/rustfuture/repository-intelligence#measured-results) · [Reproducibility](https://github.com/rustfuture/repository-intelligence#reproducibility)

### [RSI Experimental Framework](https://github.com/rustfuture/rsi-experimental-framework)

Controlled infrastructure for iterative model-guided candidate generation, validation, evaluation, and selection with reproducible accounting. No general RSI or intelligence-improvement claim is made.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rustfuture/rsi-experimental-framework/blob/main/notebooks/rsi_open_weight_colab.ipynb) · [Experiment Status](https://github.com/rustfuture/rsi-experimental-framework#experiment-status) · [Results](https://github.com/rustfuture/rsi-experimental-framework#measured-results)

### [RLT-RSI Experiment](https://github.com/rustfuture/rlt-rsi-experiment)

Looped-transformer experiments with bounded **RSI-style iterative adaptation**, recurrent depth, and post-selection held-out evaluation.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rustfuture/rlt-rsi-experiment/blob/main/notebooks/rlt_rsi_colab.ipynb) · [Research questions](https://github.com/rustfuture/rlt-rsi-experiment/blob/main/DESIGN.md#research-questions) · [RSI-style mode](https://github.com/rustfuture/rlt-rsi-experiment#rsi-style-iterative-adaptation)

### [Model Adaptation Lab](https://github.com/rustfuture/model-adaptation-lab)

Reproducible model-adaptation experiments on Rust compiler-error explanations, including preserved negative results and CI-verified dataset manifests.

[![Open validation in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rustfuture/model-adaptation-lab/blob/main/notebooks/validation_colab.ipynb) · [Negative-result report](https://github.com/rustfuture/model-adaptation-lab/blob/main/reports/negative-result.md) · [Correctness boundaries](https://github.com/rustfuture/model-adaptation-lab#correctness-levels)

## Other Systems & Utilities

- [deltasafe](https://github.com/rustfuture/deltasafe) — Authenticated file-transfer prototype for trusted LANs, with bounded frames, explicit integrity checks, and verified file publication.
- [grainx](https://github.com/rustfuture/grainx) — Terminal system monitor in Rust with an optional loopback HTTP metrics service and JSON/CSV export.
- [RustHound](https://github.com/rustfuture/RustHound) — Streaming log-analysis CLI with configurable pattern, frequency, and correlation rules.

## Approach

Experiments are documented with committed artifacts and reproducible commands, and system
boundaries are stated explicitly rather than left implied. Negative and inconclusive results
stay in the record when they are part of the evidence.

## Contact & Collaboration

- **GitHub**: Open an issue or discussion on the respective repository.
- **Focus Areas**: Agent runtime safety, deterministic verification gates, evaluation reproducibility, and low-overhead Rust systems.
