# Nonlinear Language Design: Cognitive Science Study

A research project exploring whether nonlinear structured language can improve AI cognitive efficiency in physics problem-solving.

## Overview

This project compares linear text problems with nonlinear structured format problems to measure:
- Response time
- Accuracy
- Stability

## Results (Problem 1-10)

| Metric | Linear | Nonlinear | Improvement |
|--------|--------|-----------|-------------|
| Response Time | 0.996s | 0.417s | ↓ 58.2% |
| Accuracy | 86.7% | 100.0% | ↑ 13.3% |
| Stability | 100% | 100% | Equivalent |

## Setup

```bash
pip install -r requirements.txt
export OPENAI_API_KEY="your-api-key-here"
```

## Run Experiments

```bash
# Problem 1-10
python3 new_problem_1_10_experiment.py

# Problem 11-20
python3 problem_11_20_experiment.py

# Problem 21-30
python3 problem_21_30_experiment.py
```

## Files

- `new_problem_1_10_experiment.py` - Experiment for problems 1-10
- `problem_11_20_experiment.py` - Experiment for problems 11-20
- `problem_21_30_experiment.py` - Experiment for problems 21-30
- `physics_problems_collection.py` - Linear language problems
- `nonlinear_problem_1.md` - Nonlinear language problems
- `config.py` - Configuration (not in git, use environment variables)

## License

MIT License
