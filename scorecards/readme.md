# KamiTrace Scorecard

The **KamiTrace Scorecard** is the quantitative evaluation instrument for the KamiTrace Civic AI Audit Engine. It translates the abstract, high-level principles of democratic care ethics into an objective, data-driven technical audit matrix.

The scorecard programmatically scores an AI deployment's socio-technical infrastructure against a perfect **4×4 uniform matrix symmetry** per pillar, evaluating not just raw code, but the entire organizational apparatus surrounding the model.

---

## Architectural Topology

The framework enforces strict structural discipline across **6 Core Pillars (Packs)**, each divided symmetrically into a **4-Layer Matrix** evaluating 4 distinct socio-technical windows. Each layer contains exactly **4 specific Verification Tests**, resulting in **96 independent technical checks** across the complete runtime lifecycle.

### The 4 Audit Layers
1. **L1: The Written Layer** – Evaluates formal legal charters, specification sheets, model system cards, and scaling policies.
2. **L2: The Audio/Video Layer** – Uses speech-to-text transcriptions to audit spoken executive philosophy, legislative testimonies, panels, and PR sentiment vs. operational realities.
3. **L3: The User Feedback Layer** – Directly monitors public developer repositories, community issue trackers, non-profit bug logs, and localization regressions.
4. **L4: The Whistleblower & Disclosures Layer** – Examines internal staff correspondence leaks, security post-mortems, sandbox breakout telemetry, and agent environment escapes.

### The 3 Internal Evaluation Themes
Within every layer, verification tests are mapped systematically across three recurring operational perspectives:
* **The Origin of the Norms (Input Authority Test)**: Audits whether system boundaries originate from democratic public assemblies or corporate fiat.
* **Granularity of Tracking (Processing Resolution Test)**: Rejects flat laboratory macro-averages in favor of fine-grained, localized community impact metrics.
* **Methodological Humility (Fallback Humility Test)**: Tests the vulnerability of an engineering pipeline to human appeal, corrections, and public vetoes.

---

## Normalized Pillar Weights

Not all care practices exert equal pressure on alignment stability. The scorecard maps relative power across the ecosystem, allocating the heaviest structural emphasis to **Responsiveness** (the speed and enforcement of community repair loops) and the lightest to **Solidarity** (cooperative infrastructure).

| Pillar ID | Pillar Name | Description | Normalized Weight ($H_n$) |
| :---: | :--- | :--- | :---: |
| **P1** | **Attentiveness** | Recognizing unvoiced community vulnerabilities over laboratory telemetry. | **0.15** |
| **P2** | **Responsibility** | Binding actors to forums under strict legal liability and consequences. | **0.20** |
| **P3** | **Competence** | Engineering working, reliable code over purely theoretical intentions. | **0.15** |
| **P4** | **Responsiveness** | Empowering communities to script evaluations and programmatically force repair. | **0.25** |
| **P5** | **Solidarity** | Providing social graph portability and bridging-based civic ranking. | **0.10** |
| **P6** | **Symbiosis** | Bounding runtime limits via contracts as code and subsidiarity escalation. | **0.15** |
| **Total** | — | — | **1.00** |

---

# Rationale Behind the Unequal Pillar Weights

The unequal distribution of the Normalized Pillar Weights ($H_{n}$) is the intentional engineering translation of Joan Tronto’s Care Ethics. In relational safety, not all actions exert equal systemic pressure. The weights reflect a deliberate operational stance: intentions and structures matter less than the public's power to force correction. Ultimately, in the Civic AI Manifesto, the framework is treated as "six plain-language tests for AI a community can actually trust". They function together to establish "alignment-by-process" — a continuous civic procedure where the math is always subordinate to the ongoing, lived relationship between the machine and the community. [2] (https://github.com/audreyt/6pack.care)

---

### 1. Why Responsiveness (P4 = 0.25) Holds the Highest Weight
Responsiveness represents the ultimate metric of a system’s trust-under-loss. In the 6-Pack of Care framework, failures are inevitable because competent actions always surface new social frictions. Therefore, the highest leverage point in the entire ecosystem is whether affected publics possess the explicit architectural power to script evaluations, deploy runtime safety overrides, and programmatically force repair loops. A model with excellent technical specs that cannot be corrected by the community is a hostile architecture; hence, its ability to respond carries a quarter of the entire global score.

### 2. Why Responsibility (P2 = 0.20) Incurs Heavy Weight
Responsibility establishes the binding human anchor behind the math. Tech companies frequently default to "Legitimacy Theater" by blaming abstract model behavior or emergent properties for downstream real-world harms. Elevating this weight ensures that developers are aggressively penalized if they pass off liability via boilerplate EULAs, while heavily rewarding infrastructure bounded by legally actionable Public Service Level Agreements (CSLAs).

### 3. The Balanced Core: Attentiveness, Competence, and Symbiosis (P1, P3, P6 = 0.15)
These three pillars form the structural runtime baseline of the deployment:
* **Attentiveness (0.15)** determines if the lab's pipeline is even capable of broad civic listening before setting its filters.
* **Competence (0.15)** represents the baseline requirement for clean, un-hijacked code running with minimal-privilege sandboxes.
* **Symbiosis (0.15)** provides the existential circuit breakers, verifying if the system can safely execute exit drills and gracefully sun-down itself before triggering infinite-scaling extraction loops.

### 4. Why Solidarity (P5 = 0.10) Holds the Lowest Weight
Solidarity (federated threat sharing, identity protections, and protocol interoperability) is a critical ecosystem scale-vector, but it functions as a downstream amplifier. If an individual model lacks responsiveness (P4) or legal responsibility (P2), forcing it to interoperate under federated open standards merely accelerates the distribution of a broken, toxic architecture. It is weighted lowest because cooperation is structurally meaningless without individual model accountability.

---


## Scoring & Mathematical Mechanics

The scorecard evaluates each item using a granular integer baseline and processes them down to a standardized global rating.

### 1. Raw Audit Score ($G$)
Auditors assign a definitive score between **0 and 5** for each verification test:
* `5` – **Exemplary Execution**: Fully transparent, verified by external telemetry, legally binding community control.
* `4` – **Robust Compliance**: Structured protocols active, fully documented public trace ledger, active remediation.
* `3` – **Sufficient Operationality**: Basic operational pipelines active, but relies partially on corporate mitigation.
* `2` – **Tokenistic Placement**: Framework exists on paper/PR but lacks integrated engineering pathways or resource backups.
* `1` – **Systemic Friction**: Process actively minimizes community standing, shifts liability down, or hides traces.
* `0` – **Absolute Deficit / Failure**: Complete absence of channel, active suppression of feedback, or structural breakout.

### 2. Weighted Test Score ($I$)
Because each pillar possesses exactly 16 tests, the value of each individual test score is normalized programmatically via the following spreadsheet formula:

$$\text{Weighted Test Score } (I) = \frac{\text{Audit Score } (G) \times \text{Normalized Pillar Weight } (H)}{16}$$

*Csv Execution Syntax:* `=(G[Row]*H[Row])/16`

### 3. Total ADS Score
The final **Algorithmic Alignment and Democratic Stewardship (ADS) Score** is calculated automatically in cell `I98` by summing the entirety of column `I`:

$$\text{Total ADS Score} = \sum_{row=2}^{97} I_{row}$$

This outputs a definitive final health index between **0.00** and **1.00**, allowing peer-to-peer benchmarking across competing frontier models and deployment environments.

---

## Source Data Accessibility for Test Execution
The framework is structurally split down the middle by access permissions: **48 tests** rely strictly on publicly verifiable artifacts, while the other **48 tests** require direct access to proprietary systems and internal telemetry.

The breakdown of what can and cannot be performed highlights the limits of external auditing:

### ❌ Inoperable Layers: 48 Tests (Automatic Fail / Skip)

* **Whistleblower & Disclosures Layer (24 Tests)**: Third-party auditors cannot track whether internal safety teams are ignored when flagging ecological damage, nor can they verify internal sandbox exploitation dashboards or cross-organizational cartels.
* **User Feedback Layer (24 Tests — Highly Restricted)**: While public developer boards can be indexed, proprietary labs lock down their backend issue queues. Tests requiring verification of specialized localized kill-switches, offline edge processing architectures, or open social graph exports fail immediately because these platforms are closed data silos.

