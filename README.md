# HECKTOR Centre-Aware Prognosis

This project explores survival prediction for head and neck cancer using HECKTOR-style clinical data.

## Project goal

The main goal is to build a prognosis pipeline that can later support centre-aware validation, where a model is trained on some centres and tested on an unseen centre.

## Current work

The project currently includes:

- Python and survival-analysis foundations
- Kaplan-Meier analysis
- Cox proportional hazards modelling
- synthetic multi-centre validation
- centre-wise evaluation
- real clinical-data survival modelling
- cross-validation and reporting

## Real clinical dataset

A public MDA clinical dataset was used for the real-data survival experiment.

- Patients: 156
- Outcome: Overall survival
- Final features:
  - Age
  - Sex
  - HPV status

## Final validated model

Model:

- Cox proportional hazards model
- Penalizer: 1.0

Validation:

- 5-fold cross-validation
- Random seed: 42

Mean C-index:

- 0.615

## Centre-aware validation

True centre-aware validation requires real multi-centre data.

The current real MDA dataset appears to represent one centre, so centre-aware validation is demonstrated using the synthetic multi-centre pipeline.

## Results

Main result files are stored in:

```text
results/