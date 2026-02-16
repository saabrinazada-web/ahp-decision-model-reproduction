# Analytical Hierarchy Process (AHP) Decision Model Reproduction

## Project Overview

This project presents a computational reproduction of the Analytical Hierarchy Process (AHP) decision model originally developed in an academic report for workplace selection.

The objective of this implementation is to ensure computational transparency, methodological validation, and full reproducibility of the decision-making framework using Python.

All calculations are implemented programmatically, including:

- Pairwise comparison matrix normalization
- Priority vector estimation
- Maximum eigenvalue approximation (λ_max)
- Consistency Index (CI)
- Consistency Ratio (CR)
- Global priority synthesis

The final ranking produced by this implementation matches the original analytical results.

---

## Methodological Framework

The Analytical Hierarchy Process (AHP) follows a structured multi-criteria decision-making approach:

1. Define the decision goal
2. Identify evaluation criteria
3. Construct pairwise comparison matrices
4. Normalize matrices
5. Estimate priority vectors
6. Validate consistency (CR ≤ 0.10)
7. Synthesize global priorities

Consistency validation is performed for every matrix to ensure decision reliability.

---

## Criteria Evaluated

The decision model evaluates four primary criteria:

- Salary
- Career Growth
- Facilities
- Location

Each criterion is assessed using pairwise comparison based on Saaty’s scale.

---

## Alternatives Evaluated

Five workplace alternatives are assessed under each criterion:

- PT. SAI
- PT. JAI
- PT. HWT
- BPR
- Western

---

## Results Summary

### Criteria Weights

- Career Growth: 41.2%
- Salary: 37.7%
- Facilities: 13.8%
- Location: 7.3%

Consistency Ratio (CR): 0.0581  
The matrix is considered consistent (CR < 0.10).

### Final Ranking

1. PT. SAI — 26.28%
2. PT. HWT — 20.80%
3. Western — 19.87%
4. PT. JAI — 18.47%
5. BPR — 14.58%

The ranking aligns with the original analytical findings.

---

## Technical Implementation

The project is structured modularly:

- `config.py` → stores input matrices
- `ahp_calculation.py` → contains core AHP functions
- `main.py` → execution pipeline
- `requirements.txt` → dependency management

The implementation is fully reproducible and can be executed with:
python main.py


---

## Dependencies

- Python 3.x
- numpy
- pandas
- tabulate

Install dependencies with:
pip install -r requirements.txt


---

## Reproducibility Statement

This implementation ensures that all AHP calculations are transparently computed and validated programmatically, eliminating manual computational bias and improving analytical reliability.

The project demonstrates structured decision modeling, consistency validation, and weighted aggregation using a clean, modular architecture.

