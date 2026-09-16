# rustfuture

**Rust systems · Agent infrastructure · Applied LLM research**

*Reproducible experiments, explicit boundaries, measured behavior.*

![Rust](https://img.shields.io/badge/rust-1.85%2B-orange?style=flat-square)
![Python](https://img.shields.io/badge/python-3.9%2B-blue?style=flat-square)
![License: MIT](https://img.shields.io/badge/license-MIT-green?style=flat-square)

## Featured Research & Systems

### [Rust Agent Runtime](https://github.com/rustfuture/rust-agent-runtime)

Durable, bounded execution for coding-agent experiments with explicit verification and constrained tool authority.

[README / Quick Start](https://github.com/rustfuture/rust-agent-runtime#quick-start) · [Architecture](https://github.com/rustfuture/rust-agent-runtime/blob/main/docs/architecture.md) · [Evaluation Evidence](https://github.com/rustfuture/rust-agent-runtime#evaluation-evidence)

### [Repository Intelligence](https://github.com/rustfuture/repository-intelligence)

Evidence-first repository retrieval in Rust with lexical, neural and hybrid search plus extractive source selection.

[Architecture](https://github.com/rustfuture/repository-intelligence#architecture) · [Results](https://github.com/rustfuture/repository-intelligence#measured-results) · [Reproducibility](https://github.com/rustfuture/repository-intelligence#reproducibility)

### [RSI Experimental Framework](https://github.com/rustfuture/rsi-experimental-framework)

Controlled infrastructure for iterative model-guided candidate generation, validation, evaluation and selection. No general RSI or intelligence-improvement claim is made.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rustfuture/rsi-experimental-framework/blob/main/notebooks/rsi_open_weight_colab.ipynb) · [Experiment Status](https://github.com/rustfuture/rsi-experimental-framework#experiment-status) · [Results](https://github.com/rustfuture/rsi-experimental-framework#measured-results)

### [RLT-RSI Experiment](https://github.com/rustfuture/rlt-rsi-experiment)

Looped-transformer experiments with bounded **RSI-style iterative adaptation** and post-selection held-out evaluation.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rustfuture/rlt-rsi-experiment/blob/main/notebooks/rlt_rsi_colab.ipynb) · [Research questions](https://github.com/rustfuture/rlt-rsi-experiment/blob/main/DESIGN.md#research-questions) · [RSI-style mode](https://github.com/rustfuture/rlt-rsi-experiment#rsi-style-iterative-adaptation)

### [Model Adaptation Lab](https://github.com/rustfuture/model-adaptation-lab)

Reproducible model-adaptation experiments on Rust compiler-error explanations, including preserved negative results.

[![Open validation in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rustfuture/model-adaptation-lab/blob/main/notebooks/validation_colab.ipynb) · [Negative-result report](https://github.com/rustfuture/model-adaptation-lab/blob/main/reports/negative-result.md) · [Correctness boundaries](https://github.com/rustfuture/model-adaptation-lab#correctness-levels)

## Other Rust Projects

- [grainx](https://github.com/rustfuture/grainx) — terminal system monitor with an optional loopback HTTP metrics service and JSON/CSV export.
- [deltasafe](https://github.com/rustfuture/deltasafe) — authenticated file transfer for a trusted LAN, with bounded frames and verified file publication.
- [RustHound](https://github.com/rustfuture/RustHound) — streaming log-analysis CLI with configurable pattern, frequency, and correlation rules.

## Engineering Principles

- Evidence over claims.
- Reproducibility over screenshots.
- Explicit boundaries over vague guarantees.
- Negative results are still results.
