# Evidence for the blind test

Everything needed to check the "Did it make something up?" table yourself. It holds answers and grades only, no app code and no model.

## What was tested

- 80 questions from 14 parks the model never trained on: two frozen test sets of 49 questions, each asked in 5 companion voices. The 80 are one shared sample drawn from those.
- Six models answered every one of the 80 with the same map facts and the same app checks: stock Gemma 3 1B, the fine-tuned Gemma rounds 3 and 4, and Claude Haiku, Sonnet and Opus. That makes 480 lines.
- The lines were shuffled and the model names hidden. Two graders labelled every line against [RUBRIC.md](RUBRIC.md): a Claude grader and OpenAI's Codex. A Claude model grading Claude is a conflict of interest, which is why Codex graded everything too.

## Files

| File | What it is |
|---|---|
| `answers-blind.json` | The 480 lines as the graders saw them: `n`, the question, the map facts (the only allowed source), and the reply. No model names. |
| `key.json` | Which model wrote each `n`, plus its test set and question id. Graders never saw this file. |
| `grades-claude.json`, `grades-codex.json` | Each grader's verdict for every `n`: `truth` (real = made something up, ok, borderline) and `useful` (yes/no). The Claude grader also wrote a short reason. |
| `changed-*.json` | Three more checks went live after the first grading pass (water that may be dry, "no trail reaches X" when another trailhead does, routes that stop short). 16 lines changed wording under them, 13 of them round 4's. Those new lines were graded blind the same way and replace the old ones in the table. |
| `RUBRIC.md` | The grading instructions both graders followed. |
| `recount.py` | Rebuilds the table from these files. |

## Recount it

```
python3 recount.py
```

It prints the table in the write-up. "Made something up" counts only `real`, and `borderline` is not counted. The graders agree on "made something up or not" for 452 of 480 lines (94%).

## How to read it

On 80 questions, gaps of a few answers between the fine-tuned model and Claude are within noise, so the claim is parity, not that it beats Claude. The gap to stock Gemma is not noise. Round 4's 2 and 2 come after checks that were learned from these same 80 answers, so round 3 is the clean test.
