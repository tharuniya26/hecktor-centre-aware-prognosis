# Clinical-Only Overall Survival Prediction in an MDA Head and Neck Cancer Cohort: An Exploratory Cox Model Study

Tharuniya Anpalakan  
Department of Applied Sciences  
Northumbria University  
Newcastle upon Tyne, United Kingdom  
w25070895@northumbria.ac.lk

**Abstract?**This exploratory study describes a clinical-only Cox proportional hazards analysis of overall survival in an MDA clinical head and neck cancer dataset. The table contains 156 unique patient records, 43 recorded deaths, and 113 censored observations. A Cox model with age, sex, and encoded HPV status, using a penalizer of 1.0, achieved a saved mean five-fold cross-validated concordance index (C-index) of **0.615498** with random seed **42**. HPV status was missing for 116 of 156 patients; the current dummy encoding does not distinguish missing HPV from the reference category. Candidate feature sets were compared using cross-validation, and the selected model has no independent external test or reported uncertainty interval. Separately, a 12-patient synthetic example demonstrates the mechanics of leave-one-centre-out evaluation; its scores are not clinical results. These findings describe an exploratory clinical baseline for overall survival and do not establish performance on unseen real centres or the value of imaging features.

**Index Terms—**overall survival, head and neck cancer, Cox proportional hazards, clinical prediction, cross-validation.

## I. Introduction

This paper reports what the repository's completed analyses support: an exploratory clinical-only model for **overall survival** and a separate synthetic example of a centre-held-out evaluation pipeline. Published work describes an MD Anderson head and neck squamous cell carcinoma (HNSCC) cohort archived by The Cancer Imaging Archive (TCIA) with clinical and survival information [1]. The HECKTOR 2022 overview places MD Anderson data within the broader PET/CT and outcome-prediction challenge [2]. These sources provide background context; they do not establish the derivation of the local CSV.

The contribution is a transparent account of the available cohort, implemented modelling steps, saved validation metric, and limitations. The repository protocol proposes recurrence-free survival and PET/CT radiomics comparisons, but those experiments were not completed. The synthetic example illustrates evaluation code only; it does not provide real multi-centre validation.

## II. Data and Methods

### A. Real clinical table and outcome

The analysed local table is an MDA-labelled clinical dataset with 156 patient records and 84 variables. Published work describes an MD Anderson HNSCC cohort available through TCIA with clinical and survival data [1]; however, the exact provenance and derivation of the local `mda_train_clinical_info.csv` were **not independently re-verified** here. The analysis uses `Survival  (months)` as duration and `Overall Survival Censor` as the event indicator. Its 43 values of 1 correspond to records labelled `Dead`; its 113 values of 0 correspond to records labelled `Alive`. The measured endpoint in this analysis is **overall survival**, in months. Inclusion criteria beyond what the local table establishes remain unverified. No centre identifier or real centre-held-out test is used in the completed analysis.

**TABLE I — Real clinical cohort and analysis variables**

| Item | Value |
|---|---:|
| Unique patient records | 156 |
| Recorded deaths (event = 1) | 43 |
| Censored observations (event = 0) | 113 |
| Outcome | Overall survival, months |
| Model predictors | Age, sex, encoded HPV status |
| HPV status recorded | 40/156 (29 positive; 11 negative) |
| HPV status missing | 116/156 |

### B. Real-data modelling and validation

The notebook selects age, sex, HPV status, survival time, and event status. It applies `pandas.get_dummies(..., drop_first=True)` to sex and HPV status and then drops rows with missing values. Because the HPV dummy `HPV status_positive` is zero both for recorded HPV-negative entries and for missing HPV entries, this encoding **does not distinguish missing HPV from the reference category**. All 156 rows remain in the resulting model table. The final model uses Cox proportional hazards methodology [3] with a penalizer of 1.0.

The notebook evaluates prognostic discrimination using a concordance index [4] with five-fold cross-validation and seed 42. The saved result is the arithmetic mean of its five fold C-indices: **0.615498**. The repository does not save those five seeded fold scores separately, an uncertainty interval, or independent external-test predictions.

Exploratory candidate feature sets were compared using cross-validation. The selected age, sex, and HPV model must therefore be treated as exploratory: its reported cross-validation mean is not an independent confirmation of the choice. The notebook also calculates apparent C-indices on the data used to fit an age-only model and a larger multivariable model. These are labelled as training results in Table II.

### C. Synthetic centre-aware pipeline demonstration

A separate hand-entered example contains 12 patients assigned to synthetic centres A, B, and C, with four patients per centre. The demonstration holds out each centre in turn, learns HPV and T-stage missing-value replacements from the training portion, fits a Cox model with age, HPV-positive indicator, and T stage, and scores the held-out example patients. The pipeline uses a Cox penalizer of 0.1 for the reported centre-wise scores. These artificial records and scores are separate from the MDA clinical table and cannot assess real cross-centre generalization.

**Fig. 1 — Analysis workflow (to be drawn in the LaTeX manuscript):** two separate branches, one for the real MDA overall-survival five-fold cross-validation and one for the 12-patient synthetic leave-one-centre-out pipeline.

## III. Results

### A. Real MDA overall-survival analysis

The saved final result is a **mean five-fold cross-validated C-index of 0.615498 (seed 42)** for the clinical-only Cox model. This is a discrimination estimate from internal cross-validation, not evidence of clinical utility or external-centre performance. The age-only and larger multivariable values below were measured on their training data; their differing feature sets and validation methods prevent a like-for-like performance comparison with the selected model.

**TABLE II — Real MDA overall-survival model results**

| Model | Predictors | Evaluation | C-index |
|---|---|---|---:|
| Age-only Cox | Age | Apparent training | 0.568 |
| Larger multivariable Cox, penalizer 0.1 | Age, sex, site, histology, grade, T, N, HPV status | Apparent training | 0.760 |
| Selected clinical Cox, penalizer 1.0 | Age, sex, encoded HPV status | Mean five-fold cross-validation, seed 42 | **0.615498** |

The notebook also evaluated an age, sex, HPV status, and grade candidate using the same seeded five-fold approach. Its reported mean was approximately 0.563434. Because feature sets were compared on cross-validation results, neither that contrast nor the selected result constitutes independent model confirmation.

### B. Synthetic pipeline demonstration

The synthetic centre-held-out scores are shown solely to document operation of the pipeline. Each held-out group has four example patients. The mean of the three reported centre C-indices is 0.244333; it is **not** an estimate of real multi-centre performance. The synthetic notebook also records convergence warnings during unpenalized exploratory fits, consistent with the very small example size.

**TABLE III — Synthetic centre-aware pipeline demonstration only**

| Synthetic held-out centre | Example patients | C-index |
|---|---:|---:|
| A | 4 | 0.200 |
| B | 4 | 0.333 |
| C | 4 | 0.200 |

## IV. Discussion

The real analysis provides a recorded internal cross-validation result for a limited clinical predictor set. Its mean C-index of 0.615498 should be interpreted cautiously because HPV status is mostly missing and encoded with the reference category, candidate feature sets were compared using cross-validation, and there is no independent external test. The apparent training values in Table II cannot be read as held-out results.

The synthetic demonstration verifies that centre splitting, training-only missing-value replacement, model fitting, and held-out scoring can be executed on the example data. Its numerical scores are not evidence about patient prognosis or robustness across real centres. No PET/CT image features, radiomics, multimodal model, or recurrence-free-survival experiment is reported here.

## V. Limitations and Future Work

The completed real experiment addresses overall survival only. The local table does not support a completed real centre-held-out experiment, and the repository has no independent external test set for the selected model. The final C-index has no reported uncertainty interval, and only one seeded five-fold split is saved. Candidate feature-set comparison used cross-validation; the selected model is exploratory and not independently confirmed. The notebook does not report a final-model proportional-hazards diagnostic or calibration assessment.

HPV status is missing for 116/156 patients. The current encoding maps missing HPV and the recorded reference category to the same dummy value, so the fitted HPV coefficient and model performance require caution. A future analysis should encode HPV missingness explicitly or perform training-fold-only imputation, with all preprocessing fitted independently within each cross-validation fold, prespecify the model-selection process, and report uncertainty. Real centre-aware validation would require identified patients from multiple real centres and a held-out-centre design. PET/CT radiomics and recurrence-free-survival studies remain future work, subject to suitable data and an appropriate protocol.

## VI. Conclusion

The completed repository work supports an exploratory, clinical-only overall-survival Cox analysis in 156 records from the analysed MDA clinical dataset, with a saved mean five-fold cross-validated C-index of **0.615498** at seed **42**. The separate 12-patient synthetic example demonstrates centre-aware pipeline mechanics only. Neither result establishes real multi-centre generalization, imaging benefit, or clinical utility.

## References

[1] A. J. Grossberg *et al.*, "Imaging and clinical data archive for head and neck squamous cell carcinoma patients treated with radiotherapy," *Scientific Data*, vol. 5, art. no. 180173, 2018. doi: 10.1038/sdata.2018.173.

[2] V. Andrearczyk *et al.*, "Overview of the HECKTOR Challenge at MICCAI 2022: Automatic Head and Neck Tumor Segmentation and Outcome Prediction in PET/CT," in *Head and Neck Tumor Segmentation and Outcome Prediction: Third Challenge, HECKTOR 2022, Held in Conjunction with MICCAI 2022, Proceedings*, Lecture Notes in Computer Science, vol. 13626, pp. 1–30, 2023. doi: 10.1007/978-3-031-27420-6_1.

[3] D. R. Cox, "Regression Models and Life-Tables," *Journal of the Royal Statistical Society: Series B*, vol. 34, no. 2, pp. 187–202, 1972. doi: 10.1111/j.2517-6161.1972.tb00899.x.

[4] F. E. Harrell Jr., R. M. Califf, D. B. Pryor, K. L. Lee, and R. A. Rosati, "Evaluating the Yield of Medical Tests," *JAMA*, vol. 247, no. 18, pp. 2543–2546, 1982. doi: 10.1001/jama.1982.03320430047030.

