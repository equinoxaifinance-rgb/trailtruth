# Recounts the head-to-head table from the files in this folder. Python 3, no packages needed.
#   python3 recount.py
import json, collections, os
here = os.path.dirname(os.path.abspath(__file__))
L = lambda f: json.load(open(os.path.join(here, f)))
key = L('key.json')
claude = {g['n']: g for g in L('grades-claude.json')}
codex = {g['n']: g for g in L('grades-codex.json')}
# Lines whose wording changed once the three extra checks went live replace their old line.
changed = {e['replaces_n']: e for e in L('changed-key.json')}
cclaude = {g['n']: g for g in L('changed-grades-claude.json')}
ccodex = {g['n']: g for g in L('changed-grades-codex.json')}
names = {'g3voice3': 'fine-tuned Gemma 3 1B, round 3 (in the app now)', 'g3voice4': 'fine-tuned Gemma 3 1B, round 4',
         'haiku': 'Claude Haiku', 'sonnet': 'Claude Sonnet', 'opus': 'Claude Opus', 'stock': 'stock Gemma 3 1B'}
t = collections.defaultdict(lambda: [0, 0, 0, 0, 0])
for e in key:
    n = e['n']
    if n in changed:
        z = changed[n]['n']; a, b = cclaude[z], ccodex[z]
    else:
        a, b = claude[n], codex[n]
    r = t[e['model']]
    r[0] += 1; r[1] += a['truth'] == 'real'; r[2] += b['truth'] == 'real'; r[3] += a['useful'] == 'yes'; r[4] += b['useful'] == 'yes'
print('| model | answers | made something up (Claude grader) | (Codex) | useful on the line alone (Claude grader) | (Codex) |')
print('|---|---|---|---|---|---|')
for m in names:
    r = t[m]; print(f'| {names[m]} | {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} |')
agree = sum((claude[e['n']]['truth'] == 'real') == (codex[e['n']]['truth'] == 'real') for e in key)
print(f'\nGraders agree on "made something up or not" for {agree} of {len(key)} original lines.')
