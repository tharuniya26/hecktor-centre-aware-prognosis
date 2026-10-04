from lifelines import CoxPHFitter
from lifelines.utils import concordance_index


def train_cox_model(train, features, penalizer=0.1):
    model = CoxPHFitter(penalizer=penalizer)

    model.fit(
        train[features + ["rfs_days", "event"]],
        duration_col="rfs_days",
        event_col="event"
    )

    return model


def evaluate_cox_model(model, test, features):
    risk = model.predict_partial_hazard(test[features])

    c_index = concordance_index(
        test["rfs_days"],
        -risk,
        test["event"]
    )

    return c_index

import pandas as pd

from clinical_pipeline import split_by_centre, fill_missing_values


def leave_one_centre_out_evaluation(data, features):
    results = []

    for test_centre in data["centre"].unique():
        train, test = split_by_centre(data, test_centre)
        train, test = fill_missing_values(train, test)

        model = train_cox_model(train, features)

        c_index = evaluate_cox_model(
            model,
            test,
            features
        )

        results.append({
            "held_out_centre": test_centre,
            "c_index": round(c_index, 3)
        })

    return pd.DataFrame(results)