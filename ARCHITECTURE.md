# KamiTrace Core Repository Architecture Playbook

## Rule Set Description & Architectural Strengths
The KamiTrace framework treats governance documentation as a structured, deterministic code asset rather than freeform prose. The strict alignment of this logical and linguistic architecture provides three vital advantages to public-interest watchdogs and engineers:
* **Machine-Checkable Invariants:** Keeping layer names, explanations, and section keys completely static across all files allows for automated linting and regression testing via continuous integration (CI) pipelines.
* **Contextual Balance:** Forcing section explanations to pivot while section names remain rigid prevents the framework from becoming purely abstract, ensuring the auditor is always focused on the unique socio-technical constraints of that specific care phase.
* **Rigorous Cross-File De-duplication:** Establishing cross-file text reviews ensures that intersecting corporate behaviors (such as executive compliance under questioning) do not cross-contaminate fields, maintaining an un-biased mathematical score.

---

## Invariant Integrity & Consistency Rules

### 1. Global Document & File Structure
* **File Naming Standard:** Files must be stored using a strictly sequential, lowercase snake-case syntax: `XX_pillarname_action.md` (e.g., `01_attentiveness_recognition.md`).
* **H1 Header Syntax:** Every file must begin with an absolute Level 1 header tracking the specific index, Joan Tronto care phase, and corresponding Civic AI action: `# Pillar [X]: [Tronto Virtue Phase] ([Civic AI Action Target])`.
* **Philosophical Definition Layout:** A standardized block describing the relational safety dimensions and the singular *Core Question for the Test* must immediately follow the H1 header.

### 2. Checklist Layers (The 4 Media Footprints)
* **Invariant Text Match:** The master checklist header, the layer names, and the layer explanations must remain 100% identical and unchanged across all six pillar files.
* **Heading Standard:** All media footprint layers must be formatted using a Level 3 header (`###`).
* **Approved Layer Strings & Explanations:**
  * `### Checklist Layer 1: The Written Layer`
    * *Explanation Line:* This audit window evaluates legal governance frameworks, technical model specification sheets, release notes, and formal scaling policies.
  * `### Checklist Layer 2: The Audio & Video Layer`
    * *Explanation Line:* This audit window reviews recorded panels, broadcast press briefings, public-facing interviews, and formal legislative testimony.
  * `### Checklist Layer 3: The User Feedback Layer`
    * *Explanation Line:* This audit window monitors grassroots issue logs, non-profit community trackers, and public-facing developer repository threads.
  * `### Checklist Layer 4: The Whistleblower & Disclosures Layer`
    * *Explanation Line:* This audit window examines internal staff correspondence leaks, security post-mortems, and anomalous agent environment escapes.

### 3. Invariant Sections (The 3 Analytical Vectors)
* **Linguistic Division Rule:** Section headings must enforce a strict structural separation between the *Philosophical Domain* (the text before the parenthesis) and the *Analytical Vector / Code Key* (the text inside the parenthesis). 
* **Heading Standard:** All section headings must be formatted using a Level 4 header (`####`).
* **Approved Invariant Section Strings:**
  * `#### Section 1: The Origin of the Norms (Input Authority Test)`
  * `#### Section 2: Granularity of Tracking (Processing Resolution Test)`
  * `#### Section 3: Methodological Humility (Fallback Humility Test)`
* **Contextual Evolving Explanations:** A short sentence explaining the specific architectural focus of that vector *must* follow the heading. This line must change for every pillar file to capture the unique care dimensions, and it must be audited to ensure zero repetitive phrasing or duplicate strings across different pillars.

### 4. Mathematical Weighting & Metric Constraints
* **The 4-Metric Layer Budget:** Every single layer within every pillar file must contain exactly **4 verification metrics**. Leaving a layer with 3 metrics or expanding a layer to 5 metrics breaks the spreadsheet's uniform divisor math and invalidates the audit matrix.
* **Paired Test Vector Standard:** To fit 4 metrics uniformly into 3 invariant sections, a paired test vector (2 tests) must be assigned to a specific designated section per layer.
* **Metric Tagging Syntax:** All test items must use a strict, machine-searchable checkbox syntax prefix for simple regex filtering: 
  * `*   [ ] **[Verification Test X.X] [Test Name]**`

### 5. Final Compilation Quality Gate
* **Cross-File Deduplication Audit:** Once all six markdown assets are drafted, a global programmatic or manual text search must be performed across the entire workspace directory. Any matching strings, copied validation questions, or duplicate criteria found between different files must be stripped or reallocated to preserve strict data independence.
