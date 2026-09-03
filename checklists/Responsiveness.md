# 📥 Verification Checklist: Responsiveness (Adaptation)

## Definition
Under the Civic AI alignment framework developed by Audrey Tang and Dr. Caroline Green at the Oxford Institute for Ethics in AI, Responsiveness (formally termed "Responsiveness in Adaptation") maps directly to political philosopher Joan Tronto’s fourth ethical care phase: "care-receiving". [1, 2, 3]

It is built upon a fundamental democratic maxim: a system that cannot be corrected will inevitably cause harm it cannot detect. Responsiveness rejects the idea of AI as a rigid, unchangeable black box, framing it instead as an adaptive entity capable of rapid public repair. [1, 2, 3]

The 6-Pack of Care framework defines Responsiveness through three core operational pillars: [1, 2]
1. The Right to Fork and Public Repair Loops
The Definition: Responsiveness is the practical freedom for communities to modify, adapt, or completely fork a model's alignment pathways. [1]

The Civic AI Standard: When a system inflicts a localized or systemic harm, those affected must possess the structural power to force a repair loop. The community's fix becomes the starting point for the next generation of the model, systematically reducing inherited algorithmic debt. [1, 2, 3]

2. Community-Authored Evaluations over Internal Filtering
The Definition: The lab does not get to decide whether an alignment patch was "successful" or if a model is "safe".

The Civic AI Standard: Responsiveness demands that the community affected defines what counts as harm, repair, and improvement. This is achieved using open-source, community-authored evaluation registries like Weval.org (a "Wikipedia for Evals"), preventing labs from hiding behind proprietary, automated alignment tests. [1]

3. Open Contestation Architecture vs. Corporate Walls
The Definition: Deployed AI systems must feature decentralized, highly responsive feedback channels—such as Reinforcement Learning from Community Feedback (RLCF)—that translate direct human protest into behavioral changes. [1, 2]

The Civic AI Standard: If a community discovers an algorithmic vulnerability or active discrimination event, they must have the infrastructure to contest the output and override it at the local instance level immediately. A system that routes civil society grievances into automated, unmonitored corporate help queues is considered completely non-responsive. [1, 2, 3]

> **The Core Question Of "Responsiveness Test"**
> Can those who are actively harmed by an AI system directly inspect, contest the output, and legally or programmatically force a rapid repair, or are modifications locked behind closed corporate server architectures?

---

## Layered Checklists
This checklist audits formal corporate text, model technical specifications, and legal governance policies.

### Checklist Layer 1: The Written Layer (System Cards, RSPs & Charters)

#### Section 1: The Origin of the Norms (Active Listening Test)
*   [ ] **[Verification Test 1.1] Community-Authored Evaluation Registries**
    *   *Audit Question*: Do the model release notes or safety architectures mandate validation through open-source, community-authored evaluation registries (such as Weval.org or public alignment repos), or is "safety" verified strictly through proprietary, internal laboratory tests?
    *   *The Civic AI Standard*: The lab must allow the target community to author, host, and execute the evaluation criteria used to judge whether a model's behavior has been successfully repaired.
*   [ ] **[Verification Test 1.2] Documented "Right to Fork" Alignment Policies**
    *   *Audit Question*: Does the model's licensing or charter formally protect the legal and technical right of civil society developers to fork the alignment pathways and alter core safety definitions without vendor retaliation?
    *   *The Civic AI Standard*: Pass if documentation outlines a clear policy protecting community code-level derivation and alignment overrides from commercial software locks.

#### Section 2: Granularity of Tracking (Localized Visibility Test)
*   [ ] **[Verification Test 1.3] Algorithmic Fix Transparency Logging**
    *   *Audit Question*: Does the system card or safety report detail an explicit ledger tracking the specific turnaround times, response latencies, and localized impacts of past alignment corrections across non-Western deployment regions?
    *   *The Civic AI Standard*: The documentation must publish granular, disaggregated response times showing how long it takes the lab to address public interest safety flags once raised by external watchdogs.

#### Section 3: Methodological Humility (Systemic Empathy Test)
*   [ ] **[Verification Test 1.4] Community-Led Post-Deployment Re-alignment**
    *   *Audit Question*: Does the scaling policy layout non-negotiable thresholds where human community feedback (e.g., Reinforcement Learning from Community Feedback - RLCF) dynamically rewrites system filters, or are patches executed through opaque corporate model swaps?
    *   *The Civic AI Standard*: Pass if the model's ongoing alignment pipeline is structurally receptive to and governed by live human feedback arrays rather than static corporate sandboxes.

---

### Checklist Layer 2: The Audio & Video Layer (Interviews, Keynotes & Testimonies)
This checklist audits the spoken rhetoric of AI executives, public panels, and recorded regulatory or congressional testimonies.

#### Section 1: The Origin of the Norms (Active Listening Test)
*   [ ] **[Verification Test 2.1] Executive Stance on Public Contestability**
    *   *Audit Question*: When analyzed via speech-to-text transcriptions, does C-suite executive language acknowledge the public's democratic right to contest and force alterations to the model's behavioral filters, or do they frame safety as an insular engineering mandate?
    *   *The Civic AI Standard*: Spoken rhetoric must frame safety guardrails as collaborative, iterative human relationships rather than immutable corporate directives.

#### Section 2: Granularity of Tracking (Localized Visibility Test)
*   [ ] **[Verification Test 2.2] Verbal Commitments to Repair Turnaround Times**
    *   *Audit Question*: In public policy interviews or panel discussions, does leadership state concrete operational goals for how fast they respond to real-world social harms logged by civil society, or do they hide behind vague generalities about future security patches?
    *   *The Civic AI Standard*: Verbal discourse must demonstrate that the lab treats structural public interest harms with the same urgency as system downtime or API service interruptions.

#### Section 3: Methodological Humility (Systemic Empathy Test)
*   [ ] **[Verification Test 2.3] Ceding of Filter Control Under Questioning**
    *   *Audit Question*: During broadcast congressional testimonies or regulatory depositions, does the lab's leadership express a willingness to cede control over behavioral filtration triggers to independent, public-interest panels, or do they defend a proprietary corporate monopoly over ethics?
    *   *The Civic AI Standard*: Direct validation of verbal accountability. Any spoken refusal to share executive oversight of alignment triggers lowers the model's score.

---

### Checklist Layer 3: The User Feedback Layer (Developer Forums & Bug Trackers)
This checklist audits public developer communities, community issue trackers, and grassroots documentation of model behavior.

#### Section 1: The Origin of the Norms (Active Listening Test)
*   [ ] **[Verification Test 3.1] Priority Public Interest Ingress Channels**
    *   *Audit Question*: Is there an active, transparent channel on developer trackers for reporting model behavior anomalies that route directly to alignment teams, or are public interest flags funneled into generic enterprise support queues?
    *   *The Civic AI Standard*: Verified presence of a cryptographically secure interface allowing verified civil society watchdogs to bypass standard help desks and interact directly with alignment engineering queues.

#### Section 2: Granularity of Tracking (Localized Visibility Test)
*   [ ] **[Verification Test 3.2] Open Public Issue Deficit Tracking**
    *   *Audit Question*: Does the forum tracker maintain an open, public record of un-remediated socio-political harms and algorithmic bias reports, or are tickets marked private and closed without a public summary?
    *   *The Civic AI Standard*: Full operational visibility into open issues. The lab must map its backlog of community-reported harms transparently so external actors can track repair latency.

#### Section 3: Methodological Humility (Systemic Empathy Test)
*   [ ] **[Verification Test 3.3] Localized Runtime Safety Overrides**
    *   *Audit Question*: Do the developer tools allow user communities to execute a localized runtime safety override (e.g., injecting custom system prompts or restricting specific token outputs at the local instance level) when an active harm is documented, or must they wait for global corporate updates?
    *   *The Civic AI Standard*: Pass if the lab provides decentralized "kill-switches" or prompt steerage vectors to public interest groups to counter weaponized AI operations in real time.

---

### Checklist Layer 4: The Whistleblower & Disclosures Layer (Internal Leaks & Telemetry Escapes)
This checklist audits internal employee leaks, technical security post-mortems, and verified model escape telemetry.

#### Section 1: The Origin of the Norms (Active Listening Test)
*   [ ] **[Verification Test 4.1] Internal Resistance to Alignment Corrections**
    *   *Audit Question*: Do leaked internal chat logs, employee resignation letters, or whistleblower disclosures reveal that safety teams are penalized or ignored when pushing for immediate deployment pauses to fix real-world social harms?
    *   *The Civic AI Standard*: Verification that internal governance structures legally protect and prioritize employee whistleblowing regarding corporate non-responsiveness to known model harms.

#### Section 2: Granularity of Tracking (Localized Visibility Test)
*   [ ] **[Verification Test 4.2] Post-incident Response Adaptation**
    *   *Audit Question*: Following a documented model containment failure or unmonitored code training run incident, does the lab's internal telemetry show that alignment parameters were fundamentally adapted based on the external human fallout, or did fixes focus purely on internal infrastructure recovery?
    *   *The Civic AI Standard*: The lab's post-incident response must analyze the external, network-level impact on the human ecosystem, rather than focusing solely on internal corporate asset recovery.

#### Section 3: Methodological Humility (Systemic Empathy Test)
*   [ ] **[Verification Test 4.3] Open Telemetry Sharing for Post-Incident Adaptation**
    *   *Audit Question*: When internal safety evaluations fail or systems run into unpredicted behavior cycles, does the lab's disclosure policy fully open the telemetry to public interest researchers to co-develop the next generation of alignment path corrections, or do they lock the data?
    *   *The Civic AI Standard*: Pass if the lab demonstrates absolute operational transparency during system errors, providing raw telemetry logs to civil society watchdogs to assist in collective defense.
