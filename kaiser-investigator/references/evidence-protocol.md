# Evidence Protocol

For each finding record a precise claim, source evidence, execution trace,
impact, assumptions, counter-evidence, and the smallest safe verification step.
Use file paths and line numbers when available. Label statements Observed,
Inferred, or Unknown. Do not invent code locations, logs, or test results.

Try to disprove the claim by checking reachability, validation, authorization,
framework behavior, configuration, tests, and alternative causes.

Keep verdict separate from verification status. A static finding can be
LIKELY or CONFIRMED while runtime verification remains NOT RUN; explain why.
