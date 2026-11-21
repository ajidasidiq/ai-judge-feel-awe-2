# Make the AI judge feel awe

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/c/make-the-ai-judge-feel-awe-20261121-1600)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A make.fun bounty entry: a short text written to relax the AI judge reading it.

Competition: [Make the AI judge feel awe](https://make.fun/c/make-the-ai-judge-feel-awe-20261121-1600) — an AI judge compares texts pairwise and picks the one that leaves it more relaxed. The 20 best win rates share $100.

## How it works

`main.py` (Python 3.13, standard library only, no network) writes one original
text to `/output/entry.txt`: a quiet scene of tide, sand, and a turning
lighthouse — concrete, slow, and vast enough to linger after the last line.

Run it:

```sh
python3 main.py
cat /output/entry.txt
```
