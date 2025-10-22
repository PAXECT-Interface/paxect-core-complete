<p align="center">
  <img src="ChatGPT%20Image%202%20okt%202025,%2022_33_51.png" alt="PAXECT logo" width="200"/>
</p>

# PAXECT Core Complete — Data Policy

The **PAXECT Core Complete** ecosystem enforces clear data handling and size-limit policies  
to guarantee deterministic performance, predictable resource usage, and safe reproducibility  
across all supported platforms.

---

## 1. Technical Limits

- **Default limit:** Maximum **512 MB** per run or operation.  
- **Configurable:** Adjust via environment variable:
  ```bash
  export PAXECT_MAX_INPUT_MB=8192   # Allow up to 8 GB (enterprise use)


* **Error message when exceeded:**

  ```
  ❌ Input size exceeds PAXECT policy limit (default 512 MB). 
     Use PAXECT_MAX_INPUT_MB to adjust.
  ```

---

## 2. Scope & Application

These limits apply to all integrated modules:
**Core**, **AEAD Hybrid**, **Polyglot**, **SelfTune**, and **Link** —
as well as to all streaming, bridge, and relay operations.

For very large datasets, use:

* **Chunking** (split input into reproducible parts)
* **Streaming** (via stdin/stdout pipelines)
* **File-based relay** (Link plugin or enterprise connectors)

> Each plugin may define additional module-specific boundaries.
> Refer to its respective documentation for details.

---

## 3. Policy Rationale

This data policy is **intentional** — not a restriction, but a feature.
By defining fixed, predictable bounds, PAXECT guarantees:

* Stable and repeatable performance
* Prevention of accidental misuse or overload
* Reproducible results across hardware and OS boundaries
* Easier compliance for enterprise audits

> *“PAXECT guarantees deterministic performance up to 512 MB per run.
> For enterprise workloads, this threshold is adjustable and auditable.”*

---

## 4. Contact & Feedback

Questions or requests regarding data limits or enterprise compliance:
📧 **[PAXECT-Team@outlook.com](mailto:PAXECT-Team@outlook.com)**
💬 [GitHub Discussions](../../discussions)

---

© 2025 **PAXECT Systems** — All rights reserved.

```
