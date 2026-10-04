import pandas as pd

from survival_model import leave_one_centre_out_evaluation


def main():
    clinical_data = pd.DataFrame({
        "patient_id": [
            "P001", "P002", "P003", "P004",
            "P005", "P006", "P007", "P008",
            "P009", "P010", "P011", "P012"
        ],
        "centre": [
            "A", "A", "A", "A",
            "B", "B", "B", "B",
            "C", "C", "C", "C"
        ],
        "age": [63, 55, 71, 49, 66, 58, 74, 52, 61, 57, 69, 64],
        "hpv_positive": [1, 0, 1, 1, 0, 1, 0, 1, 1, None, 0, 1],
        "t_stage": [2, 3, 2, 1, 4, 2, 3, 2, 2, 3, None, 4],
        "rfs_days": [800, 250, 1200, 430, 600, 310, 500, 900, 720, 280, 650, 400],
        "event": [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1]
    })

    features = ["age", "hpv_positive", "t_stage"]

    results = leave_one_centre_out_evaluation(
        clinical_data,
        features
    )

    print(results)

    results.to_csv(
        "results/experiment_centre_wise_c_index.csv",
        index=False
    )

    print("Results saved to results/experiment_centre_wise_c_index.csv")


if __name__ == "__main__":
    main()