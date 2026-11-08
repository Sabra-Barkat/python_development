# 🐍 Python Development

> **DecodeLabs · Python Programming · Industrial Training Kit · Batch 2026**

A collection of hands-on Python projects built during my DecodeLabs industrial training. Each project lives in its own folder with its own README, source code and tests, and each one builds on the skills of the last.

---

## 📂 Projects

| # | Project | Description | Key Skills |
|:-:|---------|-------------|------------|
| 1 | [To-Do App](./project-1-todo) | Task manager with add, view and remove features, plus a bonus version | Lists, loops, functions, input handling |
| 2 | [Expense Tracker](./project-2-expense-tracker) | Records expenses and calculates totals, plus a bonus version | Data structures, calculations, validation |
| 3 | [Random Password Generator](./project-3-password-generator) | Cryptographically secure password generator with entropy analysis and a CLI | `secrets`, `string`, library integration, string manipulation |
| 4 | [Quiz App](./project-4-quiz) | Interactive quiz with scoring, plus a bonus version | Conditionals, loops, scoring logic |

> Every project includes a bonus version where available and unit tests (`test_*.py`) to verify correct behaviour.

---

## 🚀 Getting Started

**Requirements:** Python 3.8 or newer. No third-party packages are needed.

```bash
# Clone the repository
git clone https://github.com/Sabra-Barkat/python_development.git
cd python_development

# Open a project folder and run it
cd project-3-password-generator
python main.py
```

### Running the tests

```bash
# Projects 1, 2 and 4 (single-file tests)
python -m unittest test_todo.py
python -m unittest test_expense_tracker.py

# Project 3 (package with a tests/ folder)
python -m unittest discover -s tests -t . -v
```

> Each project's own README lists the exact commands, options and examples.

---

## ⭐ Featured: Project 3 – Random Password Generator

A professional-grade CLI tool that goes beyond "random characters":

- 🔐 Uses `secrets` (OS-level entropy) instead of `random` (predictable Mersenne Twister)
- ✅ Validates input and guarantees every enabled character class appears
- ⚡ Builds strings with `''.join()` for linear-time efficiency
- 📐 Reports entropy (`E = L × log₂(R)`), strength rating and estimated crack time
- 🧪 16 unit tests, zero dependencies

```text
$ python main.py -l 16 -s
[YWg^r'gnZ[RHq5^

Entropy       : 103.6 bits
Strength      : Very Strong
```

➡️ [Read the full documentation](./project-3-password-generator/README.md)

---

## 🛠 Skills Demonstrated

- Python fundamentals: variables, loops, conditionals, functions
- Working with standard-library modules (`random`, `string`, `secrets`, `math`, `argparse`)
- Input validation and error handling
- Modular project structure (Input → Process → Output)
- Unit testing with `unittest`
- Git and GitHub workflow, documentation

---

## 📬 Contact

**Sabra Barkat**
GitHub: [@Sabra-Barkat](https://github.com/Sabra-Barkat)

---

<p align="center"><b>Built during the DecodeLabs Industrial Training Kit · Batch 2026</b></p>
