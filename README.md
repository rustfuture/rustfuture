# rustfuture

**Rust systems · Agent infrastructure · Applied LLM research**

*Reproducible experiments, explicit boundaries, measured behavior.*

![Rust](https://img.shields.io/badge/rust-1.85%2B-orange?style=flat-square)
![Python](https://img.shields.io/badge/python-3.9%2B-blue?style=flat-square)

## Featured Research & Systems

### [Reflex Control](https://github.com/rustfuture/reflex-control)

A research prototype System-1 control plane and policy engine in Rust for AI agent runtimes, arbitrating whether an execution step can proceed autonomously or must escalate to a frontier model. On a 100-task held-out synthetic partition with live Jev signals, it recorded 0/43 false accepts and 66% autonomous coverage in a single run.

[README / Quick Start](https://github.com/rustfuture/reflex-control#quick-start) · [Architecture](https://github.com/rustfuture/reflex-control#workspace-architecture) · [Evaluation Benchmark](https://github.com/rustfuture/reflex-control#evaluation-benchmark--measured-results) · [Runnable Examples](https://github.com/rustfuture/reflex-control#runnable-examples)

### [Rust Agent Runtime](https://github.com/rustfuture/rust-agent-runtime)

A research prototype task runtime and evaluation harness in Rust for autonomous coding-agent experiments, separating model decisions from execution authority with crash-recoverable task state and bounded subprocess execution.

[README / Quick Start](https://github.com/rustfuture/rust-agent-runtime#quick-start) · [Architecture](https://github.com/rustfuture/rust-agent-runtime/blob/main/docs/architecture.md) · [Evaluation Evidence](https://github.com/rustfuture/rust-agent-runtime#evaluation-evidence)

### [Repository Intelligence](https://github.com/rustfuture/repository-intelligence)

An experimental research prototype CLI in Rust for local-first code retrieval and source selection, providing line-cited hybrid search and verbatim evidence citations instead of generative prose.

[Architecture](https://github.com/rustfuture/repository-intelligence#architecture) · [Results](https://github.com/rustfuture/repository-intelligence#measured-results) · [Reproducibility](https://github.com/rustfuture/repository-intelligence#reproducibility)

### [RSI Experimental Framework](https://github.com/rustfuture/rsi-experimental-framework)

A research prototype testbed in Python studying iterative candidate generation, evaluation, and selection with deterministic accounting and held-out isolation. It evaluates keyword-policy mutations over a fixed synthetic pool and makes no general self-improvement claim.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rustfuture/rsi-experimental-framework/blob/main/notebooks/rsi_open_weight_colab.ipynb) · [Experiment Status](https://github.com/rustfuture/rsi-experimental-framework#experiment-status) · [Results](https://github.com/rustfuture/rsi-experimental-framework#measured-results)

### [RLT-RSI Experiment](https://github.com/rustfuture/rlt-rsi-experiment)

An experimental research prototype benchmark comparing conventional and shared-weight looped transformers on binary sequence parity. It evaluates recurrent depth, length generalization, and bounded loop-schedule adaptation with post-selection held-out evaluation.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rustfuture/rlt-rsi-experiment/blob/main/notebooks/rlt_rsi_colab.ipynb) · [Research questions](https://github.com/rustfuture/rlt-rsi-experiment/blob/main/DESIGN.md#research-questions) · [RSI-style mode](https://github.com/rustfuture/rlt-rsi-experiment#rsi-style-iterative-adaptation)

### [Model Adaptation Lab](https://github.com/rustfuture/model-adaptation-lab)

A research prototype testbed and evaluation harness for local LoRA adaptation, deterministic baselines, and negative results on structured Rust compiler-error explanations. It includes family-disjoint dataset validation and preserves a historical negative adaptation result.

[![Open validation in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rustfuture/model-adaptation-lab/blob/main/notebooks/validation_colab.ipynb) · [Negative-result report](https://github.com/rustfuture/model-adaptation-lab/blob/main/reports/negative-result.md) · [Correctness boundaries](https://github.com/rustfuture/model-adaptation-lab#correctness-levels)

## Other Systems & Utilities

- [deltasafe](https://github.com/rustfuture/deltasafe) — Experimental CLI prototype in Rust for authenticated, tamper-evident file transfer across trusted local networks with bounded frames and staged atomic publication.
- [grainx](https://github.com/rustfuture/grainx) — Experimental terminal system monitor and local loopback HTTP metrics service in Rust with process inspection and JSON/CSV snapshot export.
- [RustHound](https://github.com/rustfuture/RustHound) — Experimental CLI log analyzer in Rust for inspecting log streams to detect operational anomalies using pattern, frequency, and correlation rules.

## Approach

Experiments are documented with committed artifacts and reproducible commands, and system
boundaries are stated explicitly rather than left implied. Negative and inconclusive results
stay in the record when they are part of the evidence.

## Contact & Collaboration

- **GitHub**: Open an issue or discussion on the respective repository.
- **Focus Areas**: Agent runtime safety, deterministic verification gates, evaluation reproducibility, and low-overhead Rust systems.
