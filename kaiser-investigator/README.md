# KAISER Investigator

Evidence-driven debugging skill for repository-aware AI coding agents.

## Install
Extract this archive so the `kaiser-investigator/` folder is placed in your
agent's supported skills directory. The exact location depends on the agent.
Open the repository you want to investigate, then invoke `kaiser-investigator`
or ask the agent to use this skill.

## Workflow
Evidence → Trace → Challenge → Fix → Test → Verdict.

KAISER helps investigate the actual repository. It does not guarantee every
bug will be found or every fix will work. Run relevant tests and report actual
results. The bundled JavaScript files are synthetic examples, not a benchmark
or evidence of real-project performance.

## Included files
- `SKILL.md`: main instructions and manifest.
- `references/`: evidence protocol, cross-stack tracing, and safety guidance.
- `examples/`: intentionally vulnerable and corrected synthetic example with tests.
- `scripts/`: simple manually labelled verdict agreement scorer and sample input.
- `assets/`: reusable finding report template.
- `LICENSE`: MIT licence.

## Evaluation caveat
`scripts/score_eval.py` compares manually supplied expected and predicted
verdict labels only. It does not run an agent, grade evidence quality, or
establish overall accuracy. Do not present its sample input as benchmark data.

## Safety
The skill defaults to read-only inspection and requires explicit authorization
before executing repository code or making risky changes.
