# Project Summary

## Project title

HECKTOR Centre-Aware Prognosis

## Aim

To develop a survival prediction pipeline for head and neck cancer using HECKTOR-style clinical data, with emphasis on centre-aware validation and robustness across unseen centres.

## What was completed

- Python and survival-analysis foundations
- Kaplan-Meier analysis
- Cox proportional hazards modelling
- synthetic multi-centre validation
- leave-one-centre-out evaluation
- real MDA clinical survival modelling
- 5-fold cross-validation
- model comparison
- reproducible reporting
- GitHub project organization

## Real-data experiment

Dataset:
- MDA clinical data
- 156 patients

Final features:
- Age
- Sex
- HPV status

Model:
- Cox proportional hazards
- Penalizer: 1.0

Validation:
- 5-fold cross-validation
- Seed: 42

Final mean C-index:
- 0.615

## Main limitation

The available real dataset appears to represent a single centre.

Therefore, true centre-aware validation on real multi-centre HECKTOR data could not yet be performed.

The centre-aware workflow was instead demonstrated using synthetic multi-centre data.

## Future work

- obtain authorized multi-centre HECKTOR data
- add PET and CT imaging features
- extract radiomics
- combine imaging and clinical features
- evaluate leave-one-centre-out performance
- compare clinical-only vs multimodal models