# Crosswalk — changelog

## v0.9 — 2026-09-12

First content revision since the v0.8 launch (2026-05-21). 93 → 102 delta cards.

### Added — applicability dates on every card
Every card now carries a `When:` line. The original page said *what* each target adds
without saying *when* it bites, which read as if all of it were live. It is not.

### Added — three new cards (×3 bases = 9 cards)
| Target | Card | Why it was missing |
|---|---|---|
| EU AI Act | **AI literacy (Art. 4)** | Applies since 2 Feb 2025 to every provider and deployer, not just high-risk. The most widely breached AI Act duty, and absent from v0.8. |
| GDPR | **Enforcement procedure** — Reg. (EU) 2025/2518 | Adopted 26 Nov 2025 (after v0.8 was written); applies 2 Apr 2027. 15-month investigation deadline, early settlement, harmonised admissibility. |
| HIPAA | **Security Rule overhaul (NPRM)** | 90 FR 898 (6 Jan 2025). Flagged `PROPOSED RULE — NOT ENFORCEABLE`; the single most-asked HIPAA question and absent from v0.8. |

### Corrected
- **"Omnibus VII (2026-05-07)"** — a pre-adoption label — replaced everywhere with the
  adopted instrument: **Digital Omnibus on AI, Regulation (EU) 2026/1744** (OJ 2026-07-27,
  CELEX 32026R1744). Stand-alone (Annex III) high-risk deferred to **2027-12-02**;
  product-embedded (Annex I) to **2028-08-02**. Art. 5 gains the AI-generated NCII/CSAM
  prohibition from **2026-12-02**.
- **HIPAA breach notification** — v0.8 said "60-day clock to individuals and HHS". Wrong for
  the HHS leg: 45 CFR 164.408 requires notice to the Secretary within 60 days only for
  breaches affecting ≥500 individuals; under 500 are logged and submitted annually within
  60 days after the end of the calendar year. Media notice (164.406) added.
- **HIPAA patient access** — 30 days, **extendable once by 30 days** on written notice. The
  extension was missing. Amendment timing (164.526) and the six-year accounting (164.528) added.
- **GDPR Art. 8** — v0.8 said Member States "may lower the threshold to 13". They may set a
  lower age but **not below 13**, so the operative range is 13–16 and is per-Member-State.
- **GDPR cross-border transfers** — v0.8 cited Schrems II but not the adequacy decision that
  actually carries most US traffic. Added **Commission Implementing Decision (EU) 2023/1795**
  (EU–US DPF), with the per-recipient self-certification caveat, plus a `Watch:` note on the
  EDPB's 31 Jul 2026 letter to the Commission following *Trump v. Slaughter* (29 Jun 2026).
  Worded so it cannot be read as a withdrawal that has not happened.
- **AI Act Art. 50** — now stated as live since 2 Aug 2026, with 2 Dec 2026 identified as the
  Art. 50(2) transitional deadline for synthetic-content systems already on the market before
  2 Aug 2026 — *not* a general marking deadline.
- Removed an unverifiable "~60–70% overlap (GLACIS, EU AI Compass)" claim from the
  NIST AI RMF → AI Act summary.
- Per-target card counts in the summaries corrected (they had drifted).

### Page fixes
- Replaced the live `[beehiiv embed pending — paste form iframe here]` placeholder with a real
  subscribe CTA to `https://www.cybereyeq.com/subscribe` (the `www` host — the apex 404s on
  any path under GoDaddy forwarding).
- Deep links: `#<base>/<target>` (e.g. `#iso27001/hipaa`) selects and shares one pairing.
- Meta line no longer breaks apart on long regulation names.
- Print styles extended to the new `When:` and flag elements.

### Sources
EUR-Lex (Reg. (EU) 2024/1689, 2026/1744, 2025/2518, Implementing Decision (EU) 2023/1795);
European Commission AI Act Service Desk implementation timeline; European Parliament
Legislative Train (2025/0360(COD)); HHS/OCR breach-notification and Security Rule NPRM pages;
Federal Register 90 FR 898; EDPB.
