import pandas as pd
import matplotlib.pyplot as plt
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
    summary = pd.DataFrame([{
        "mean_c_index": results["c_index"].mean(),
        "std_c_index": results["c_index"].std(),
        "min_c_index": results["c_index"].min(),
        "max_c_index": results["c_index"].max()
    }])

    summary.to_csv(
        "results/experiment_summary_metrics.csv",
        index=False
    )

    print("Summary saved to results/experiment_summary_metrics.csv")
    results.plot(
        x="held_out_centre",
        y="c_index",
        kind="bar",
        legend=False
    )

    plt.ylabel("C-index")
    plt.title("Held-out Centre Performance")
    plt.ylim(0, 1)

    plt.savefig(
        "results/experiment_centre_wise_c_index.png",
        bbox_inches="tight"
    )

    plt.close()

    print("Plot saved to results/experiment_centre_wise_c_index.png")
if __name__ == "__main__":
    main()