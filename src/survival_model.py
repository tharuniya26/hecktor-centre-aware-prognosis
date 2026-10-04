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