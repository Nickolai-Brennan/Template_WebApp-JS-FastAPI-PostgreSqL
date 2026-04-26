# skill-creator Source Files

Vendored source target for Anthropic's `skill-creator` skill.

Source repository:
https://github.com/anthropics/skills/tree/main/skills/skill-creator

License:
Apache License 2.0. Keep `LICENSE.txt` with this folder when copying files.

## Files to mirror

| Target Path | Source URL |
|---|---|
| `Skills/skill-creator/SKILL.md` | https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md |
| `Skills/skill-creator/LICENSE.txt` | https://github.com/anthropics/skills/blob/main/skills/skill-creator/LICENSE.txt |
| `Skills/skill-creator/agents/grader.md` | https://github.com/anthropics/skills/blob/main/skills/skill-creator/agents/grader.md |
| `Skills/skill-creator/agents/analyzer.md` | https://github.com/anthropics/skills/blob/main/skills/skill-creator/agents/analyzer.md |
| `Skills/skill-creator/agents/comparator.md` | https://github.com/anthropics/skills/blob/main/skills/skill-creator/agents/comparator.md |
| `Skills/skill-creator/assets/eval_review.html` | https://github.com/anthropics/skills/blob/main/skills/skill-creator/assets/eval_review.html |
| `Skills/skill-creator/eval-viewer/generate_review.py` | https://github.com/anthropics/skills/blob/main/skills/skill-creator/eval-viewer/generate_review.py |
| `Skills/skill-creator/eval-viewer/viewer.html` | https://github.com/anthropics/skills/blob/main/skills/skill-creator/eval-viewer/viewer.html |
| `Skills/skill-creator/references/schemas.md` | https://github.com/anthropics/skills/blob/main/skills/skill-creator/references/schemas.md |
| `Skills/skill-creator/scripts/aggregate_benchmark.py` | https://github.com/anthropics/skills/blob/main/skills/skill-creator/scripts/aggregate_benchmark.py |
| `Skills/skill-creator/scripts/generate_report.py` | https://github.com/anthropics/skills/blob/main/skills/skill-creator/scripts/generate_report.py |
| `Skills/skill-creator/scripts/improve_description.py` | https://github.com/anthropics/skills/blob/main/skills/skill-creator/scripts/improve_description.py |
| `Skills/skill-creator/scripts/package_skill.py` | https://github.com/anthropics/skills/blob/main/skills/skill-creator/scripts/package_skill.py |
| `Skills/skill-creator/scripts/quick_validate.py` | https://github.com/anthropics/skills/blob/main/skills/skill-creator/scripts/quick_validate.py |
| `Skills/skill-creator/scripts/run_eval.py` | https://github.com/anthropics/skills/blob/main/skills/skill-creator/scripts/run_eval.py |
| `Skills/skill-creator/scripts/run_loop.py` | https://github.com/anthropics/skills/blob/main/skills/skill-creator/scripts/run_loop.py |
| `Skills/skill-creator/scripts/utils.py` | https://github.com/anthropics/skills/blob/main/skills/skill-creator/scripts/utils.py |

## Import command

From a local checkout of your repo:

```bash
git clone https://github.com/anthropics/skills.git /tmp/anthropic-skills
mkdir -p Skills/skill-creator
cp -R /tmp/anthropic-skills/skills/skill-creator/* Skills/skill-creator/
git add Skills/skill-creator
git commit -m "Vendor Anthropic skill creator"
git push
```
