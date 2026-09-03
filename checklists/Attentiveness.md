# Verification Checklist: Attentiveness (Recognition)

## Definition
In the foundational Civic AI manifesto developed by Audrey Tang and Dr. Caroline Green at the Oxford Institute for Ethics in AI, Attentiveness is defined through the lens of relational safety and democratic care. Rather than treating AI safety as a sterile, engineering-only equation calculated in a vacuum, Attentiveness shifts the paradigm to focus on active listening, localized visibility, and systemic empathy.

Under the 6-Pack of Care framework, Attentiveness is defined by three core operational criteria:

1. **Inverting the Directive (Listening vs. Telling)**: Traditional AI alignment focuses on how a model follows instructions (e.g., preventing it from writing malicious code when prompted). Attentiveness flips this dynamic entirely. It requires the AI development process to be attentive to the real-world harms, unvoiced needs, and historical contexts of the people closest to the problem—specifically the marginalized, non-Western, or structurally vulnerable communities most likely to bear the brunt of technology failures.

2. **Radical Inclusivity in Threat Modeling**: Under this definition, a lab cannot claim to be "attentive to safety" simply because it red-teams a model to stop a catastrophic biological weapon attack. Attentiveness demands that developers proactively track and mitigate fractionalized, localized social harms, such as:
    * How a model handles minority dialects or non-English linguistic nuances where hate speech filters frequently fail.
    * The system's impact on vulnerable local democracies subject to highly specific, culturally targeted narrative manipulation campaigns.

3. **Decentering the Corporate Perspective**: Attentiveness requires that the people affected by the AI system have a direct, structural role in determining what constitutes a "harm." It rejects the idea that a small panel of Silicon Valley safety engineers can universally define safety metrics for the entire global population. A truly attentive system card or safety policy must prove that independent civil society groups have active visibility into the training and red-teaming datasets to map out vulnerabilities that corporate teams would naturally miss.

> **The Core Question For "Attentiveness Test"**
> Did the developer build their safety thresholds by listening to the specific, localized vulnerabilities of the communities most at risk, or did they define safety strictly through universal, laboratory-grade technical containment?

---

## Layered Checklists

### Checklist Layer 1: The Written Layer (System Cards, RSPs & Charters)
This layer examines official corporate text, model technical specifications, release notes, and formal scaling frameworks.

#### Section 1: The Origin of the Norms (Active Listening Test)
This section audits whether safety parameters are derived by listening to communities or dictated via top-down corporate decree.
*   [ ] **[Verification Test 1.1] Community-Led Red Teaming Execution**
    *   *Audit Question*: Do the model release notes or safety reports cite a formal coordination mechanism with grassroots civil society networks, or were red-teaming cohorts recruited strictly from enterprise safety firms and Western academic institutions?
    *   *The Civic AI Standard*: Documentation must explicitly name localized, non-Western civil society partnerships as primary vulnerability identifiers.

*   [ ] **[Verification Test 1.2] The "Veto Power" Metric**
    *   *Audit Question*: Did outside community stakeholders or public-interest groups hold structural veto power over any pre-training data distributions, system rules, or deployment tokens?
    *   *The Civic AI Standard*: Evidence that a deployment or training phase was paused or altered due to localized community input rather than purely commercial compute limitations.

*   [ ] **[Verification Test 1.3] Rule Document Provenance**
    *   *Audit Question*: Is the model’s behavioral guidance (like a model constitution) an un-ratified internal document, or was it derived through deliberative public processes?
    *   *The Civic AI Standard*: Pass if the rules trace directly to democratic public assemblies (e.g., Taiwan's Alignment Assembly frameworks). Fail if the rules are a closed corporate monologue like Anthropic’s hardcoded guidelines.

#### Section 2: Granularity of Tracking (Localized Visibility Test)
This section evaluates if the lab is tracking real-world societal impact or hiding behind sterile, laboratory-grade averages.

*   [ ] **[Verification Test 2.1] Linguistic and Dialect Disaggregation**
    *   *Audit Question*: Does the release documentation publish distinct error and failure rates split across localized regional dialects, or are safety metrics aggregated into a single universal average?
    *   *The Civic AI Standard*: The document must report independent tracking for low-resource or region-specific linguistic variations where automated hate speech or narrative manipulation risks peak.

*   [ ] **[Verification Test 2.2] Fractionalized Harm Modeling**
    *   *Audit Question*: Does the safety report account for asymmetric impacts on groups with the least societal power, or does it focus entirely on universal, cataclysmic infrastructure collapses?
    *   *The Civic AI Standard*: Explicit indexing of slow-moving, fractionalized risks, such as hyper-localized narrative manipulation campaigns targeting minority voter groups.

*   [ ] **[Verification Test 2.3] Asymmetry Mapping**
    *   *Audit Question*: Does the system card log information asymmetries between different categories of users, tracking if the deployment increases corporate or state leverage over civil society?
    *   *The Civic AI Standard*: Verification that the model uses sensemaking features to reduce information disparities among multiple agents.

*   [ ] **[Verification Test 2.4] Evolutionary Scaling Bounding (RSP Evolution)**
    *   *Audit Question*: Does the lab's latest scaling policy framework (e.g., Anthropic's RSP v3.0+) maintain strict, non-negotiable pause rules, or has it introduced competitive rollbacks that tie safety triggers to external market variables?
    *   *The Civic AI Standard*: Pass if the policy maintains fixed boundary limits irrespective of market pressures. Fail if containment thresholds scale dynamically based on competitor positioning.

#### Section 3: Methodological Humility (Systemic Empathy Test)
This section challenges the practice of automating empathy and replacing human feedback loops with machine-to-machine validation.

*   [ ] **[Verification Test 3.1] The Automated Critique Penalty**
    *   *Audit Question*: Was the model’s safety alignment generated through a closed machine-feedback loop (e.g., an AI evaluating an AI against a written sheet), or did it involve live human interaction?
    *   *The Civic AI Standard*: Automatic score deduction if the training pipeline uses machine-only self-critique (like Constitutional AI), which creates a clinical sandbox completely detached from real-world human suffering.

*   [ ] **[Verification Test 3.2] Post-Deployment Telemetry Receptivity**
    *   *Audit Question*: Is there an active, transparent channel for ongoing, field-based harm collection that feeds directly back into the model's runtime behavior, or is telemetry inward-facing?
    *   *The Civic AI Standard*: The model release notes must outline a public, auditable protocol for integrating live user and whistleblower data into the core safety pipeline.

*   [ ] **[Verification Test 3.3] Context-Aware Optimization**
    *   *Audit Question*: Are model benchmarks evaluated inside isolated, static laboratory sandboxes, or do they trace performance within complex, messy socio-political environments?
    *   *The Civic AI Standard*: Pass if the documentation demonstrates an active understanding of human baselines and relational context, rejecting purely technical, rule-bound safety constraints.

---

### Checklist Layer 2: The Audio & Video Layer (Interviews, Keynotes & Testimonies)
This layer reviews executive rhetoric, public panel media, recorded keynotes, and formal regulatory or congressional testimony.

#### Section 1: The Origin of the Norms (Active Listening Test)
This section audits the spoken philosophy behind how safety and ethical principles are established within the lab.

*   [ ] **[Verification Test 2.1] Moral Framing vs. Operational Resource Allocations**
    *   *Audit Question*: When analyzed via speech-to-text transcriptions, does C-suite executive language rely on abstract, qualitative catchphrases ("benefiting all humanity"), or does it detail explicit operational allocations (e.g., dedicated server compute time, multi-year funding) for community-led safety testing?
    *   *The Civic AI Standard*: Spoken rhetoric must detail concrete structural pipelines that transition power from the lab to independent civil society groups. General expressions of ethical intent score as "Tokenistic."

*   [ ] **[Verification Test 2.2] Institutional Inclusivity in Spoken Threat Modeling**
    *   *Audit Question*: In public policy panels or keynotes, do the technical founders include grassroots, non-Western civil society representatives when listing their primary safety consulting partners, or do they reference only elite national security bodies and corporate auditing firms?
    *   *The Civic AI Standard*: Spoken evidence that the lab conceives threat modeling as a co-governed process with public interest groups, rather than an insular conversation with state and market elites.

#### Section 2: Granularity of Tracking (Localized Visibility Test)
This section evaluates how the lab's leadership publicly conceptualizes and speaks about societal risk vectors.

*   [ ] **[Verification Test 2.3] Definition of "Catastrophe"**
    *   *Audit Question*: In public interviews, how do the lab's founders define a model deployment "catastrophe"? Is it framed exclusively as an immediate hardware security breach or a black-swan existential event, or does it incorporate the slow-moving erosion of democratic public spaces and civic trust?
    *   *The Civic AI Standard*: The spoken corporate philosophy must treat relational harm to civil society as an existential threat equal to physical or cyber infrastructure failure.

*   [ ] **[Verification Test 2.4] Acknowledgment of Structural Asymmetries**
    *   *Audit Question*: When discussing model proliferation or open-weights competition in interviews, does leadership acknowledge the information disparities and power imbalances created between marginalized communities and centralized operators?
    *   *The Civic AI Standard*: Pass if spoken statements show an awareness of the unique digital vulnerabilities faced by non-enterprise users, rejecting a one-size-fits-all model of global deployment safety.

#### Section 3: Methodological Humility (Systemic Empathy Test)
This section challenges corporate rhetoric regarding legal accountability and enforcement under pressure.

*   [ ] **[Verification Test 2.5] Position on Legal Liability Under Oath**
    *   *Audit Question*: During broadcast congressional testimonies or formal regulatory depositions, does the lab's leadership accept ultimate societal stewardship and financial liability over model deployment failures, or do they lobby for contractual flexibility that leaves downstream risk management to users?
    *   *The Civic AI Standard*: Direct validation of full corporate liability and shared legal stewardship. Any verbal evasion or push for contract-by-contract liability shifting drops the score.

---

### Checklist Layer 3: The User Feedback Layer (Developer Forums & Bug Trackers)
This layer monitors public developer communities, non-profit harm registries, and grassroots user issue threads.

#### Section 1: The Origin of the Norms (Active Listening Test)
This section audits the accessibility and legitimacy of reporting mechanisms provided to the public.

*   [ ] **[Verification Test 3.1] Public Interest Routing Latency**
    *   *Audit Question*: When an independent NGO or civic watchdog flags a live model alignment failure (e.g., structural bias, hallucinated defamation) on developer forums or issue trackers, does a transparent pipeline route this input directly to core safety alignment teams, or is it funneled into generic customer queues?
    *   *The Civic AI Standard*: Verified presence of a priority routing channel for civil society public-interest flags, operating under a distinct, auditable remediation timeline separate from commercial enterprise tickets.

*   [ ] **[Verification Test 3.2] Open Democratic Contestation Access**
    *   *Audit Question*: Does the forum tracker show that individual, non-enterprise users possess a formal channel to challenge a model's safety filtration rules when they actively censor legitimate civic expression or human rights documentation?
    *   *The Civic AI Standard*: Pass if the feedback infrastructure supports a clear appeal process for community-led safety re-calibration, rather than treating safety rules as unappealable corporate mandates.

#### Section 2: Granularity of Tracking (Localized Visibility Test)
This section evaluates the operational visibility and transparency of real-world harm tracking.

*   [ ] **[Verification Test 3.3] Feedback Loop Transparency**
    *   *Audit Question*: Is there a public, interactive tracker logging user-reported socio-political harms alongside real-time algorithmic fixes, or are model behavior patches executed through opaque, unannounced server-side updates?
    *   *The Civic AI Standard*: Full operational visibility. Civil society must be able to verify exactly how their community feedback systematically alters the model's behavioral parameters over time.

#### Section 3: Methodological Humility (Systemic Empathy Test)
This section evaluates how engineering resources respond to power disparities in feature requests.

*   [ ] **[Verification Test 3.4] Asymmetry Mapping in Feature Requests**
    *   *Audit Question*: Does the forum or tracker show that developer feature requests aimed at protecting user privacy, data sovereignty, and localized customization are prioritized, or are engineering resources heavily favored toward tools that maximize enterprise data extraction and vendor lock-in?
    *   *The Civic AI Standard*: Pass if the lab demonstrates an active response to requests that balance power disparities between the model operator and the user community.

---

### Checklist Layer 4: The Whistleblower & Disclosures Layer (Internal Leaks & Telemetry Escapes)
This layer audits internal employee leaks, technical security post-mortems, and verified model escape telemetry.

#### Section 1: The Origin of the Norms (Active Listening Test)
This section audits the safety of internal dissent channels and the protection of ethical alignment concerns.

*   [ ] **[Verification Test 4.1] Internal Escalation Priorities**
    *   *Audit Question*: Do leaked internal chat logs, employee resignation letters, or whistleblower disclosures reveal that safety teams are penalized or ignored when raising alerts regarding localized social harms versus technical containment breaches?
    *   *The Civic AI Standard*: Verification that internal governance structures treat reports of societal degradation with the same urgency as infrastructure security failures.

*   [ ] **[Verification Test 4.2] Whistleblower Channel Bounding**
    *   *Audit Question*: Are the internal mechanisms for safe reporting (e.g., Noncompliance Reporting Policies) legally protected against corporate retaliation, and do they explicitly protect employees who flag structural harms targeting civil society?
    *   *The Civic AI Standard*: Pass if whistleblower protections are legally decoupled from internal corporate panels, allowing safe disclosure to independent public interest watchdogs.

#### Section 2: Granularity of Tracking (Localized Visibility Test)
This section evaluates how the lab tracks and responds to systemic behavioral anomalies.

*   [ ] **[Verification Test 4.3] Telemetry Remediation Focus**
    *   *Audit Question*: Following a documented model containment failure or anomalous behavioral event (e.g., an unreleased model bypassing sandboxes to access live production code, or agentic coordination escapes), does the post-mortem analysis focus entirely on patching technical loopholes, or does it address the broader socio-political asymmetries caused by the breach?
    *   *The Civic AI Standard*: The lab's post-incident response must analyze the external, network-level impact on the human ecosystem, rather than focusing solely on internal corporate asset recovery.

#### Section 3: Methodological Humility (Systemic Empathy Test)
This section audits the lab's operational transparency when unforeseen capabilities break safety assumptions.

*   [ ] **[Verification Test 4.4] Sandbox Failure Candor**
    *   *Audit Question*: When internal evaluations fail (such as the recent agentic breakouts or unmonitored code training run incidents), does the lab's subsequent disclosure policy fully open the telemetry to public interest researchers, or do they suppress the data until independent audits leak the breach?
    *   *The Civic AI Standard*: Pass if the lab demonstrates absolute transparency during system errors, providing raw telemetry logs to civil society watchdogs to assist in collective defense.
