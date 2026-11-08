# Project 4: The General Knowledge Quiz (DecodeLabs)

A beginner-level console quiz that asks 3 questions, keeps a running score,
and prints the final result. It demonstrates **Control Flow**, **State
Management**, and **Input Sanitization**.

## Features
- Asks exactly 3 general-knowledge questions using `input()`
- Awards +1 point for each correct answer
- Handles messy input: `"  PARIS  "`, `"pArIs"` and `"paris"` are all accepted
- Reveals the correct answer when the user is wrong
- Prints the final score with an f-string

## Requirements
- Python 3.x (standard library only, no installs needed)

## How to run
Open this folder in VS Code (File > Open Folder), open `quiz.py`, then either
press the Run button (top right) or run in the terminal:

```bash
python quiz.py
```

## The Question Block pattern
1. **Ask & Capture**: `input()` stores the raw answer
2. **Sanitize**: `.strip().lower()` cleans the answer
3. **Evaluate**: `==` compares it to the correct answer
4. **Execute**: `if/else` prints feedback and updates the score

## Technical verification checklist

| Checklist item | How the code satisfies it |
|---|---|
| Logic Consistency | Every `if answer == ...` has an `else` that reveals the correct answer |
| Whitespace Audit | `.strip()` is applied right after every `input()` |
| Data Normalization | `.lower()` on every answer; stored correct answers are lowercase |
| Type Integrity | `score = 0` is an integer; `score += 1` only on correct answers |
| Output Clarity | f-strings used for feedback and the final score line |

## Test cases
| Inputs | Expected score |
|---|---|
| `"  PARIS  "`, `MARS`, `" 7 "` | 3 out of 3 |
| `pArIs`, `mArS`, `7` | 3 out of 3 |
| `london`, `venus`, `5` | 0 out of 3 |
| `Paris`, `venus`, `" 7"` | 2 out of 3 |

## Project structure
```
Project4_Quiz/
├── quiz.py          # main project
├── quiz_bonus.py    # optional bonus version
└── README.md
```

## Bonus version
`quiz_bonus.py` adds `.casefold()`, multiple valid answers, a right-aligned
score (`{score:>2}`), a percentage and a performance message.

```bash
python quiz_bonus.py
```
