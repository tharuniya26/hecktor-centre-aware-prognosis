# Research Protocol

## Project Title

Centre-Aware Robust Multimodal Prognosis in Oropharyngeal Cancer:
Do PET/CT Radiomics Add Generalisable Value Beyond Clinical Variables
for Recurrence-Free Survival?

## Primary Research Question

When evaluated on unseen acquisition centres, do PET and CT tumour features
provide reproducible incremental value over strong clinical baselines for
recurrence-free survival prediction?

## Primary Hypothesis

PET/CT imaging may add prognostic signal beyond clinical variables during
internal evaluation, but some apparent improvement may decrease when entire
centres are held out.

## Primary Outcome

Recurrence-free survival.

## Primary Comparison

Clinical model versus clinical + PET + CT model.

## Primary Evaluation Strategy

Centre-held-out evaluation.

## Initial Model Hierarchy

1. Clinical Cox model
2. Elastic-net Cox model
3. PET radiomics model
4. CT radiomics model
5. PET + CT model
6. Clinical + PET + CT model

## Main Evaluation Dimensions

- Discrimination
- Calibration
- Overall prediction error
- Cross-centre robustness
- Segmentation robustness
- Missing-data robustness

## Important Rule

The protocol should not be changed after seeing test-centre performance merely
to make results look better.