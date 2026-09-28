# rustfuture

**Applied LLM experiments and agent tooling, in Python and Rust.**

Everything here is experimental: research prototypes and small tools, tested on synthetic or small datasets, not production-validated. Each repo states its limits, and negative results stay in the record.

## Projects

### [Reflex Control](https://github.com/rustfuture/reflex-control)

Decides whether an AI task can finish on its own, retry, or escalate to a more expensive model. It combines fast local checks with a safety veto for risky actions. In one run on a synthetic 100-task held-out set it missed none of the 31 tasks that needed escalation (a rules-only baseline missed 23) and made no false accepts, while handling 66% of tasks autonomously.

[Quick Start](https://github.com/rustfuture/reflex-control#quick-start) · [Architecture](https://github.com/rustfuture/reflex-control#workspace-architecture) · [Evaluation](https://github.com/rustfuture/reflex-control#evaluation-benchmark--measured-results) · [Examples](https://github.com/rustfuture/reflex-control#runnable-examples)

### [Rust Agent Runtime](https://github.com/rustfuture/rust-agent-runtime)

Runs automated coding tasks with language models under timeouts, command allowlists, and required verification tests. Task state is rebuilt from an append-only event log, so a crashed run can resume.

[Quick Start](https://github.com/rustfuture/rust-agent-runtime#quick-start) · [Architecture](https://github.com/rustfuture/rust-agent-runtime/blob/main/docs/architecture.md) · [Evaluation Evidence](https://github.com/rustfuture/rust-agent-runtime#evaluation-evidence)

### [Repository Intelligence](https://github.com/rustfuture/repository-intelligence)

Searches local code and returns verbatim source lines for a question instead of generating prose. Every accepted quote matched the source, but relevance is not guaranteed: the recorded 42-question run had 12 false accepts. Supports text, hash-embedding, and local neural-model search over a saved index.

[Architecture](https://github.com/rustfuture/repository-intelligence#architecture) · [Results](https://github.com/rustfuture/repository-intelligence#measured-results) · [Reproducibility](https://github.com/rustfuture/repository-intelligence#reproducibility)

### [RSI Experimental Framework](https://github.com/rustfuture/rsi-experimental-framework)

Tests an iterative propose, validate and select loop that improves keyword rules for text classification on a small synthetic dataset (32 sentences). Held-out data is scored once, after selection ends. It makes no claim beyond that toy setup.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rustfuture/rsi-experimental-framework/blob/main/notebooks/rsi_open_weight_colab.ipynb) · [Experiment Status](https://github.com/rustfuture/rsi-experimental-framework#experiment-status) · [Results](https://github.com/rustfuture/rsi-experimental-framework#measured-results)

### [RLT-RSI Experiment](https://github.com/rustfuture/rlt-rsi-experiment)

Compares standard models with models that reuse one layer several times, on deciding whether a binary sequence has an odd or even number of ones. Checks whether training on short sequences carries over to longer ones, and includes a bounded search over how many times the layer repeats.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rustfuture/rlt-rsi-experiment/blob/main/notebooks/rlt_rsi_colab.ipynb) · [Research questions](https://github.com/rustfuture/rlt-rsi-experiment/blob/main/DESIGN.md#research-questions) · [Iterative adaptation](https://github.com/rustfuture/rlt-rsi-experiment#rsi-style-iterative-adaptation)

### [Model Adaptation Lab](https://github.com/rustfuture/model-adaptation-lab)

Tests whether LoRA fine-tuning on Apple Silicon helps one small model (Qwen2.5-Coder-1.5B) explain Rust compiler errors, using a 12-record dataset and one rule-based baseline. The single recorded run showed no gain, and that negative result is kept.

[![Open validation in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rustfuture/model-adaptation-lab/blob/main/notebooks/validation_colab.ipynb) · [Negative-result report](https://github.com/rustfuture/model-adaptation-lab/blob/main/reports/negative-result.md) · [Correctness levels](https://github.com/rustfuture/model-adaptation-lab#correctness-levels)

## Smaller Rust tools

- [deltasafe](https://github.com/rustfuture/deltasafe): sends files between computers on a local network and verifies each file arrived unchanged.
- [grainx](https://github.com/rustfuture/grainx): terminal dashboard for CPU, memory, disk, network, and processes, with a local HTTP metrics endpoint.
- [RustHound](https://github.com/rustfuture/RustHound): reads log files and reports lines that match rules, repeated errors, or event sequences.

## Approach

Experiments ship with committed artifacts and the commands that reproduce them. Boundaries are stated explicitly, and inconclusive results are kept when they are part of the evidence.

## Feedback

Questions and suggestions are welcome as issues or discussions on the relevant repository.
