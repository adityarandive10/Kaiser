# KAISER Investigator 🔍

**Evidence-first debugging for AI coding agents.**

KAISER Investigator is a reusable AI agent skill that helps developers investigate software bugs, trace root causes, evaluate competing hypotheses, and recommend minimal, testable fixes backed by evidence.

Instead of guessing the cause of a bug and immediately changing code, KAISER follows a structured investigation workflow.

## 🎯 Why KAISER?

Debugging becomes difficult when an error crosses multiple layers of an application. A frontend issue may originate in an API, backend authorization logic, or database behavior.

KAISER helps coding agents investigate systematically, distinguish facts from assumptions, and report verification results honestly.

## ⚙️ Core Workflow

```text
Evidence → Trace → Challenge → Fix → Test → Verdict
```

1. **Evidence:** Inspect relevant code, logs, errors, and test results.
2. **Trace:** Follow the failing behavior across application layers.
3. **Challenge:** Compare competing explanations and look for contradictory evidence.
4. **Fix:** Recommend the smallest appropriate change.
5. **Test:** Run or propose relevant tests, subject to available tools and authorization.
6. **Verdict:** Report the findings, confidence, and verification status honestly.

## ✨ Features

- 🔎 Evidence-based root-cause investigation
- 🔗 Cross-layer tracing across frontend, API, backend, and database
- 🛡️ Security-conscious debugging practices
- 🧪 Regression-testing guidance
- 🎯 Minimal, targeted fixes instead of unnecessary rewrites
- 📋 Structured findings and investigation reports
- ⚖️ Clear distinction between confirmed causes and hypotheses

## 📂 Project Structure

```text
kaiser-investigator/
├── SKILL.md
├── README.md
├── LICENSE
├── assets/
│   └── finding-template.md
├── examples/
│   ├── status-vulnerable.js
│   ├── status-vulnerable.test.js
│   ├── status-fixed.js
│   └── status-fixed.test.js
├── references/
│   ├── evidence-protocol.md
│   ├── polyglot-tracing.md
│   └── security-guidance.md
└── scripts/
    ├── eval-example.jsonl
    └── score_eval.py
```

## 🚀 Installation

Install the published skill through the LLM SkillHub CLI:

```bash
npm install -g llmskillhub
llmsh install adityarandive2007/kaiser-investigator
```

The skill must be approved and publicly available on SkillHub for this installation command to work.

Alternatively, clone this repository:

```bash
git clone https://github.com/YOUR_USERNAME/kaiser-investigator.git
cd kaiser-investigator
```

Use the skill with a compatible coding agent by placing it in the appropriate skills directory for that agent.

## 💻 Example Use Case

Suppose a developer reports:

> Users can access a resource they should not be authorized to view.

KAISER guides the coding agent to:

- Trace the request from the frontend to the backend.
- Inspect the relevant authentication and authorization checks.
- Identify evidence supporting or contradicting possible causes.
- Recommend a minimal correction.
- Add a regression test for unauthorized access.
- Report whether the fix was actually tested.

The skill does not assume a root cause or claim a test passed without supporting evidence.

## 🧪 Examples and Evaluation

The `examples/` directory contains synthetic vulnerable and fixed JavaScript examples with corresponding tests.

The `scripts/score_eval.py` script compares verdicts against manually labelled evaluation examples. It is a simple scoring utility, not a comprehensive benchmark of AI agent accuracy.

## 🔐 Security Principles

- Do not expose credentials, tokens, or other secrets.
- Obtain appropriate authorization before executing potentially risky commands or tests.
- Avoid unnecessary changes to production systems.
- Clearly distinguish observed facts, hypotheses, and verified outcomes.
- Never fabricate test results or claim unperformed verification.

## 🛠️ Technology and Compatibility

KAISER is distributed as a `SKILL.md`-based agent skill with supporting Markdown references, JavaScript examples, tests, and a Python evaluation utility.

Its behavior depends on the capabilities and permissions of the coding agent that loads it.

## 📄 License

Released under the [MIT License](LICENSE).

## 👨‍💻 Author

**Aditya Randive**

GitHub: [@adityarandive10](https://github.com/adityarandive10)

---

**KAISER Investigator — Evidence first. Assumptions challenged. Fixes verified.**
