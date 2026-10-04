# Leakage Checklist

Before accepting any model result, check:

- [ ] Every patient appears in only one outer fold.
- [ ] Entire held-out centres are absent from model training.
- [ ] Missing-value imputation is fitted using training data only.
- [ ] Scaling is fitted using training data only.
- [ ] Feature selection is fitted using training data only.
- [ ] Hyperparameter tuning does not use the held-out centre.
- [ ] Calibration does not use the held-out centre.
- [ ] No outcome-derived feature is used as an input.
- [ ] Clinical, PET and CT data from the same patient stay together.
- [ ] Test results are not used to choose preprocessing settings.