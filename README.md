# TUF+ Problems Practice

Python DSA practice repo following the TUF+ (Take U Forward) curriculum. Solutions are written in Python using a class-based structure, with Jupyter notebooks for exploratory work.

## Structure

```
python_dsa/
├── python_basics/
│   ├── basic_maths.py         # Math problems (digits, palindrome, primes, GCD/LCM, etc.)
│   ├── basic_hashing.py       # Hashing problems (highest occurrence element, etc.)
│   ├── builtinfunctions.py    # Python built-in function practice
│   ├── python_libraries_1.py  # Standard library exploration
│   ├── python_libraries_2.py  # Standard library exploration (continued)
│   └── basics.ipynb           # Notebook scratchpad for basics
├── collections/
│   ├── Collections.ipynb      # Overview of Python collections module
│   ├── counter_practice.ipynb # Counter usage
│   ├── deque_practice.ipynb   # Deque usage
│   ├── DefaultDict.ipynb      # defaultdict usage
│   ├── OrderedDict.ipynb      # OrderedDict usage
│   └── NamedTuples.ipynb      # namedtuple usage
└── Patterns.ipynb             # Pattern printing problems
```

## Topics Covered

### Basic Maths (`basic_maths.py`)
- Count digits of a number (loop & log-based)
- Count odd digits in a number
- Reverse a number
- Palindrome number check
- Largest digit in a number
- Factorial
- Armstrong number check
- Sum of proper divisors / perfect number check
- Prime number check (brute force & optimized)
- Count of primes up to N (Sieve of Eratosthenes)
- GCD and LCM of two numbers

### Hashing (`basic_hashing.py`)
- Highest occurring element in an array

### Python Collections
- `Counter`, `deque`, `defaultdict`, `OrderedDict`, `namedtuple`

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install jupyter ipython
```