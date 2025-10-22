<p align="center">
  <img src="docs/ChatGPT%20Image%202%20okt%202025,%2022_22_22.png" alt="PAXECT logo" width="200"/>
</p>

# Contributing Guidelines — PAXECT Core Complete

Thank you for your interest in contributing to **PAXECT Core Complete**!  
This repository represents the verified reference bundle for all core PAXECT modules —  
**Core**, **AEAD Hybrid**, **Polyglot**, **SelfTune**, and **Link** — designed for deterministic, cross-platform reproducibility.

---

##  Overview

All contributions must follow the same key principles that define PAXECT:

- ✅ **Deterministic by design** — no randomness, no nondeterministic side-effects  
- ✅ **Offline-first** — no external telemetry, APIs, or network dependencies  
- ✅ **Cross-OS consistency** — must behave identically on Linux, macOS, and Windows  
- ✅ **No AI / ML components** — SelfTune is purely algorithmic, not heuristic  
- ✅ **Security hygiene** — no hard-coded secrets; all config via environment variables  

> _In short: every contribution must keep PAXECT reproducible, portable, and auditable._

---

##  Development Setup

1. **Fork this repository**
   ```bash
   git clone https://github.com/PAXECT-Interface/paxect-core-complete.git
   cd paxect-core-complete






2. **Create a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate     # Windows: venv\Scripts\activate
   ```
3. **Install dependencies**

   ```bash
   pip install -e .
   ```
4. **Run demo verification**

   ```bash
   python demos/demo_01_quick_start.py
   ```

   You should see a deterministic `[OK]` output.

---

## Contributing Workflow

1. **Create a new branch**

   ```bash
   git checkout -b feature/your-feature-name
   ```
2. **Make deterministic changes only**

   * Avoid timestamps, random UUIDs, or nondeterministic data.
   * Ensure reproducible outputs before committing.
3. **Add / update tests**

   * Include demo or validation runs when applicable.
   * Demos are preferred over unit tests for full-system verification.
4. **Commit clearly**

   ```bash
   git commit -m "Add: reproducible checksum validation for Polyglot bridge"
   ```
5. **Submit a Pull Request**

   * PRs must pass all CI checks before review.
   * Use Discussions for early feedback or design questions.

---

## Code Style & Validation

* **Language:** Python 3.9 – 3.12
* **Linting:** `flake8`, `black` (default settings)
* **Static Analysis:** CodeQL runs automatically on PRs
* **Output format:** human-readable log + JSONL state (deterministic only)

Run quick checks:

```bash
pytest -q
python demos/demo_02_integration_loop.py
```

---

## Communication

For collaboration, questions, or feature ideas:

* 💬 [GitHub Discussions](../../discussions)
* 🐛 [Issues](../../issues)
* 📧 **[PAXECT-Team@outlook.com](mailto:PAXECT-Team@outlook.com)** (for maintainers & enterprise contact)

---

## Governance

* All contributions are reviewed by maintainers under the **CODEOWNERS** policy.
* Core and brand-sensitive changes require **Owner approval**.
* By contributing, you agree to the [Code of Conduct](./CODE_OF_CONDUCT.md).

---

### Thank You!

Your contribution helps keep **PAXECT** deterministic, open, and enterprise-grade.
Let’s build reproducible innovation — together.

© 2025 **PAXECT Systems**. All rights reserved.
