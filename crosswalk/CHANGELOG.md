# Crosswalk — changelog

## v1.0 — 2026-09-12

Three new targets. 102 → **201** delta cards; 9 → 18 pairings.

| New target | Primary sources read for this build |
|---|---|
| **EU NIS2** — Directive (EU) 2022/2555 | EUR-Lex full text: Arts. 2, 3, 20, 21, 22, 23, 32, 33, 34, 41, Annexes I–II |
| **EU DORA** — Regulation (EU) 2022/2554 | EUR-Lex full text: Arts. 2, 5, 6–14, 16, 18, 19, 24, 25, 26, 28, 30, 31, 35, 42, 64 + Commission Delegated Regulation (EU) 2025/301 Art. 5 |
| **US CCPA/CPRA** — Cal. Civ. Code 1798.100 et seq. | leginfo full text: 1798.100, .120, .121, .130, .135, .140, .150, .155 + the CPPA's own announcement of the approved Cyber/Risk/ADMT regulations |

Eleven cards per new target, per base. Each carries a `When:` line, as v0.9 established.

### Facts that shaped the cards

- **NIS2 is a directive, and that is the headline.** Art. 41 set 18 Oct 2024 as the application
  date, but the binding text is each national transposing act and those landed anywhere from
  Oct 2024 (BE, IT) to **1 Oct 2026** (AT) — with DE 6 Dec 2025, HR 1 Jan 2026, SE 15 Jan 2026,
  PL 3 Apr 2026, NL 15 Aug 2026 in between. A whole card is given to this, and every other NIS2
  card's `When:` line repeats the caveat. The Jan 2026 amending proposal is carried as a `Watch:`
  note, explicitly flagged as not law.
- **Reporting clocks are the sharpest deltas.** NIS2 Art. 23(4): 24-hour early warning, 72-hour
  notification, final report within one month (trust service providers notify at 24h, not 72h).
  DORA via RTS (EU) 2025/301 Art. 5: initial notification within **four hours of classification**
  and no later than 24 hours from awareness, intermediate within 72 hours of that, final within one
  month — with the weekend/bank-holiday relief expressly unavailable to credit institutions, CCPs,
  trading venues and NIS2 essential/important entities.
- **California's new regulations are the live story.** OAL-approved 22 Sep 2025, effective
  1 Jan 2026: risk assessments run from 1 Jan 2026 with attestations due to the Agency by
  1 Apr 2028; cybersecurity-audit certifications are revenue-tiered at 1 Apr 2028 (over $100M),
  1 Apr 2029 ($50–100M), 1 Apr 2030 (under $50M); ADMT for significant decisions bites
  1 Jan 2027.
- **Sensitive personal information now includes neural data** (Cal. Civ. Code 1798.140(ae)(1)(G)).
- **The two CCPA enforcement routes differ on cure.** 1798.150's private right of action carries a
  30-day cure opportunity; 1798.155 administrative enforcement, as amended by AB 137
  (Stats. 2025, ch. 20), carries none.
- **DORA Art. 5(2)'s budget limb** — the management body must allocate and periodically review
  resilience budget — is called out, because it has no analogue in any base framework.

### Pairings worth knowing about

ISO 27001 → NIS2 is the strongest overlap anywhere on this page: Art. 21(2) reads like an Annex A
summary. SOC 2 → CCPA cybersecurity audits is the one CCPA obligation where an existing attestation
programme is a real head start. NIST AI RMF → CCPA ADMT is the only place the AI RMF carries
substantive weight against a target — and it still gives you no notice, opt-out or access right.

### Also

- `meta.verified_against` extended from 13 to **26** registry entries, including the eight national
  NIS2 transposing acts the Transposition-reality card names, and regenerated directly from
  `registry.json` rather than transcribed.
- Picker, page title, meta description and social cards updated for six targets.

Verified before publish: all 18 pairings render, 201 cards, 201 `When:` lines, no JS errors, no
horizontal overflow at 390px, deep links resolve, and `check_crosswalk_drift.py` returns clean.

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
