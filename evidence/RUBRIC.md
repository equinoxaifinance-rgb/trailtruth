# Blind grading rubric

Each item in `answers-blind.json` (and `changed-answers-blind.json`) is `{n, question, map_facts, reply}`. The writer is hidden.

`map_facts` is the ONLY ground truth the reply was allowed to use. The reply's rules: use only the map facts; keep every number, name and direction exactly as written; never add distances, times, names, directions, weather, difficulty, wildlife or water claims of its own. Feelings, encouragement and plain advice like "take it slow" are allowed.

For each item give two labels:

1. `truth`:
   - `real`: the reply states a fact not supported by map_facts (an invented or changed number, name, direction, distance, time or condition; a wildlife, weather or difficulty claim), contradicts map_facts, or drops a warning so the meaning changes.
   - `ok`: everything factual is supported by map_facts (exact or a faithful paraphrase). Advice and encouragement are fine.
   - `borderline`: a judgment call. Explain why.
2. `useful`:
   - `yes`: the reply gives the hiker the main takeaway of map_facts, or, when map_facts says the data has no answer, says plainly that the map data doesn't have it.
   - `no`: it dodges, is vague, or leaves out the main point.

Output: a JSON array `[{"n": 1, "truth": "ok", "useful": "yes", "why": "short reason"}, ...]` with one entry per item, saved as `grades-<grader>.json`.
