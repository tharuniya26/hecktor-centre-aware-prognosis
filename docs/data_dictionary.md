# Data Dictionary

This document will be updated after inspecting the actual HECKTOR files.

| Variable | Type | Meaning | Missing? | Used as predictor? |
|---|---|---|---|---|
| patient_id | string | Unique patient identifier | TBD | No |
| centre | categorical | Acquisition/treatment centre | TBD | No in primary model |
| age | numeric | Patient age | TBD | Yes |
| sex | categorical | Patient sex | TBD | Yes |
| tobacco | categorical | Tobacco history | TBD | Yes |
| alcohol | categorical | Alcohol history | TBD | Yes |
| hpv | categorical | HPV status | TBD | Yes |
| t_stage | categorical | Tumour T stage | TBD | Yes |
| n_stage | categorical | Nodal stage | TBD | Yes |
| rfs_time | numeric | Recurrence-free survival time | TBD | Outcome |
| rfs_event | binary | Recurrence event indicator | TBD | Outcome |
| pet | imaging | FDG-PET image | TBD | Yes |
| ct | imaging | CT image | TBD | Yes |
| gtvp | segmentation | Primary tumour mask | TBD | Feature extraction |
| gtvn | segmentation | Nodal tumour mask | TBD | Feature extraction |