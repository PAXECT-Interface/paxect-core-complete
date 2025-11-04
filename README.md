<p align="center">
  <img src="ChatGPT%20Image%202%20okt%202025,%2022_33_51.png" alt="PAXECT logo" width="200"/>
</p>


[![Star this repo](https://img.shields.io/badge/⭐%20Star-this%20repo-orange)](../../stargazers)
[![CI](https://img.shields.io/badge/CI-passing-brightgreen.svg)](../../actions)
[![CodeQL](https://img.shields.io/badge/CodeQL-active-lightgrey.svg)](../../actions)
[![Issues](https://img.shields.io/badge/Issues-open-blue)](../../issues)
[![Discussions](https://img.shields.io/badge/Discuss-join-blue)](../../discussions)
[![Security](https://img.shields.io/badge/Security-responsible%20disclosure-informational)](./SECURITY.md)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](./LICENSE)
<a href="https://github.com/PAXECT-Interface/paxect-core-complete/releases/latest">
  <img alt="Release" src="https://img.shields.io/github/v/release/PAXECT-Interface/paxect-core-complete?label=complete">
</a>


# 🌐 PAXECT — The Universal Deterministic Bridge  
**Build once, run anywhere.**  
Connect all operating systems and programming languages through one reproducible, offline-first runtime.  

🔗 Learn more about the ecosystem:  
👉 [**PAXECT Universal Bridge ›**](https://github.com/PAXECT-Interface/paxect-universal-bridge)


---



# PAXECT Core Complete
**Status:** v1.0.0 — Initial Public Release — October 22, 2025

**The curated PAXECT bundle:** Core + AEAD Hybrid + Polyglot + SelfTune + Link — with **10 integrated demos**, observability, and deterministic performance across OSes.

**What it is:** the official reference implementation of the PAXECT ecosystem — a verified, reproducible, cross-OS runtime that showcases the **multi-OS bridge** and **in-freq multi-channel** architecture in real workflows.

- **Unified Ecosystem:** Core + AEAD + SelfTune + Polyglot + Link in one deterministic bundle  
- **Reproducibility:** bit-identical behavior across Linux, macOS, Windows (best-effort: BSD, mobile shells)  
- **Offline-first:** zero telemetry, no network dependencies  
- **Enterprise-ready:** 10 reproducible demo pipelines, audit trail, and metrics endpoints  
- **Zero-AI Runtime:** SelfTune provides adaptive guardrails **without** ML or heuristics (no cloud)

## Relationship

- **PAXECT Core** is a **stand-alone** OS-level deterministic bridge (plugin-capable).  
- **PAXECT Core Complete** is the **curated bundle** that includes Core **plus** the official plugins and demo suite.  
Use **Core** when you want a minimal, plug-and-play bridge.  
Use **Core Complete** when you want the full experience (plugins + demos) out of the box.
---

## Installation

### Requirements
- **Python 3.9 – 3.12** (recommended 3.11+)
- Works on **Linux**, **macOS**, **Windows**, **FreeBSD**, **OpenBSD**, **Android (Termux)**, and **iOS (Pyto)**.
- No external dependencies or internet connection required — fully offline-first runtime.

### Optional Utilities
Some demos use these standard tools if available:
- `bash` (for `demo_05_link_smoke.sh`)
- `dos2unix` (for normalizing line endings)
- `jq` (for formatting JSON output)

### Install
```bash
git clone https://github.com/PAXECT-Interface/paxect-core-complete.git
cd paxect-core-complete
python3 -m venv venv
source venv/bin/activate      # on Windows: venv\Scripts\activate
pip install -e .
````

Verify the deterministic core import:

```bash
python3 -c "import paxect_core; print('PAXECT Core OK')"
```

Then run any of the integrated demos from the `demos/` folder to validate deterministic reproducibility.

---

## 📁 Repository Structure

```
paxect-core-complete/
├── paxect_core_plugin.py
├── paxect_aead_hybrid_plugin.py
├── paxect_polyglot_plugin.py
├── paxect_selftune_plugin.py
├── paxect_link_plugin.py
├── demos/
│   ├── demo_01_quick_start.py
│   ├── demo_02_integration_loop.py
│   ├── demo_03_safety_throttle.py
│   ├── demo_04_metrics_health.py
│   ├── demo_05_link_smoke.sh
│   ├── demo_06_polyglot_bridge.py
│   ├── demo_07_selftune_adaptive.py
│   ├── demo_08_secure_multichannel_aead_hybrid.py
│   ├── demo_09_enterprise_all_in_one.py
│   └── demo_10_enterprise_stability_faults.py
├── test_paxect_all_in_one.py
├── ENTERPRISE_PACK_OVERVIEW.md
├── SECURITY.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── TRADEMARKS.md
├── LICENSE
└── .gitignore
```

---

## Modules

| Module                           | Purpose                                                           |
| -------------------------------- | ----------------------------------------------------------------- |
| **paxect_core_plugin.py**               | Deterministic runtime · encode/decode · CRC32 + SHA-256 checksums |
| **paxect_aead_hybrid_plugin.py** | Hybrid AES-GCM / ChaCha20-Poly1305 encryption for data integrity  |
| **paxect_polyglot_plugin.py**    | Cross-language bridge · UTF-safe transformation between runtimes  |
| **paxect_selftune_plugin.py**    | Adaptive ε-greedy self-tuning · resource-aware control · no AI    |
| **paxect_link_plugin.py**        | Secure inbox/outbox relay · policy validation · offline file sync |

![PAXECT Architecture](paxect_architecture_brand_v18.svg)



---

## Plugins (Official)

| Plugin                         | Scope                           | Highlights                                                                   | Repo                                                                                       |
| ------------------------------ | ------------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Core**                       | Deterministic data container    | `.freq` v42 · multi-channel · CRC32 + SHA-256 · cross-OS · offline-first     | [paxect-core-plugin](https://github.com/PAXECT-Interface/paxect-core-plugin)               |
| **AEAD Hybrid**                | Encryption & Integrity          | Hybrid AES-GCM / ChaCha20-Poly1305 — fast, zero dependencies, cross-platform | [paxect-aead-hybrid-plugin](https://github.com/PAXECT-Interface/paxect-aead-hybrid-plugin) |
| **Polyglot**                   | Multi-language bridge           | Python · Node.js · Go — deterministic pipeline parity                        | [paxect-polyglot-plugin](https://github.com/PAXECT-Interface/paxect-polyglot-plugin)       |
| **SelfTune 5-in-1**            | Runtime control & observability | Guardrails, backpressure, overhead limits, metrics, and jitter smoothing     | [paxect-selftune-plugin](https://github.com/PAXECT-Interface/paxect-selftune-plugin)       |
| **Link (Inbox/Outbox Bridge)** | Cross-OS file exchange          | Shared-folder relay: auto-encode/decode `.freq` containers deterministically | [paxect-link-plugin](https://github.com/PAXECT-Interface/paxect-link-plugin)               |

**Plug-and-play:** Core operates standalone, with optional plugins attachable via flags or config. Deterministic behavior remains identical across environments.

---

## 🧪 Demo Suite (01 – 10)

Run reproducible demos from the repository root:

```bash
python3 demos/demo_01_quick_start.py
python3 demos/demo_02_integration_loop.py
python3 demos/demo_03_safety_throttle.py
python3 demos/demo_04_metrics_health.py
bash    demos/demo_05_link_smoke.sh
python3 demos/demo_06_polyglot_bridge.py
python3 demos/demo_07_selftune_adaptive.py
python3 demos/demo_08_secure_multichannel_aead_hybrid.py
python3 demos/demo_09_enterprise_all_in_one.py
python3 demos/demo_10_enterprise_stability_faults.py
```

All demos generate structured JSON audit logs under `/tmp/`, verifiable through deterministic SHA-256 outputs.

---

## Testing & Verification

Internal `pytest` suites validate core reproducibility.
End-users can rely on the integrated demo suite (01–10) for deterministic verification.
Each demo reports performance, checksum validation, and exit status cleanly.

---

## 🔒 Security & Privacy

* Default mode: **offline**, **zero telemetry**.
* Sensitive configuration via environment variables.
* AEAD Hybrid is simulation-grade; for production, integrate with verified crypto or HSM.
* Adheres to **Digital Hygiene 2027** and **NIS2** security standards.
* Follows responsible disclosure in [`SECURITY.md`](./SECURITY.md).

---

## 🏢 Enterprise Pack

See [`ENTERPRISE_PACK_OVERVIEW.md`](./ENTERPRISE_PACK_OVERVIEW.md)
for extended features and enterprise integration roadmap.

Includes:

* HSM / KMS / Vault integration
* Extended policy and audit engine
* Prometheus, Grafana, Splunk, and Kafka observability connectors
* Deployment assets (systemd, Helm, Docker)
* Compliance documentation (ISO · IEC · NIST · NIS2)

---

## 🤝 Community & Governance

* **License:** Apache-2.0
* **Ownership:** All PAXECT trademarks and brand assets remain property of the Owner.
* **Contributions:** PRs welcome; feature branches must pass deterministic CI pipelines.
* **Core merges:** Require owner approval for brand or architecture-sensitive changes.
* **Community Conduct:** See [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md)

Join as a maintainer or contributor — see [`CONTRIBUTING.md`](./CONTRIBUTING.md) for details.

---

## 🔄 Updates & Maintenance

**PAXECT Core Complete** follows an open contribution and verification-first model:

* No fixed release schedule — determinism prioritized over speed.
* Verified updates only, across OSes and environments.
* Maintainers focus on innovation, reproducibility, and architecture quality.

---

## 💠 Sponsorships & Enterprise Support

**PAXECT Core Complete** is a verified, plug-and-play runtime ecosystem unifying all PAXECT modules.
Sponsorships fund ongoing cross-platform validation, reproducibility testing, and audit compliance
for deterministic and secure data pipelines across **Linux**, **Windows**, and **macOS**.

### Enterprise Sponsorship Options

* Infrastructure validation and multi-OS QA
* Deterministic CI/CD performance testing
* OEM and observability integration partnerships
* Extended reproducibility assurance for regulated industries

### Get Involved

* 💠 [Become a GitHub Sponsor](https://github.com/sponsors/PAXECT-Interface)
* 📧 Enterprise or OEM inquiries: **enterprise@[PAXECT-Team@outlook.com](mailto:PAXECT-Team@outlook.com)**

> Sponsorships help sustain open, verifiable, and enterprise-ready innovation.

---

## Governance & Ownership

* **Ownership:** All PAXECT products and trademarks (PAXECT™ name + logo) remain the property of the Owner.
* **License:** Source code under Apache-2.0; trademark rights are **not** granted by the license.
* **Core decisions:** Architectural merges for Core and brand repos require Owner approval.
* **Contributions:** PRs reviewed under CODEOWNERS and branch protection.
* **Brand Use:** Do not use PAXECT branding for derivatives without written permission. See `TRADEMARKS.md`.

---

## Path to Paid — Sustainable Open Source

**PAXECT Core Complete** is free and open-source at its foundation.
Sustainable sponsorship ensures long-term maintenance, reproducibility, and enterprise adoption.

### Principles

* Core remains free forever — no vendor lock-in.
* Full transparency, open changelogs, and audit-ready releases.
* Global 6-month free enterprise window after public release.
* Community-driven decision-making on renewals and roadmap.

### Why This Matters

* Motivates contributors with lasting value.
* Ensures reproducible stability for enterprises.
* Balances open innovation with sustainable funding.

---

### Contact

📧 **[PAXECT-Team@outlook.com](mailto:PAXECT-Team@outlook.com)**
💬 [Issues](https://github.com/PAXECT-Interface/paxect-core-plugin/issues)
💭 [Discussions](https://github.com/PAXECT-Interface/paxect-core-plugin/discussions)

*For security disclosures, please follow responsible reporting procedures.*

Copyright © 2025 **PAXECT Systems** — All rights reserved.



