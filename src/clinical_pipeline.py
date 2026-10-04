import pandas as pd


def split_by_centre(data, test_centre):
    train = data[data["centre"] != test_centre].copy()
    test = data[data["centre"] == test_centre].copy()

    return train, test


def fill_missing_values(train, test):
    hpv_fill = train["hpv_positive"].mode()[0]
    t_stage_fill = train["t_stage"].median()

    train["hpv_positive"] = train["hpv_positive"].fillna(hpv_fill)
    test["hpv_positive"] = test["hpv_positive"].fillna(hpv_fill)

    train["t_stage"] = train["t_stage"].fillna(t_stage_fill)
    test["t_stage"] = test["t_stage"].fillna(t_stage_fill)

    return train, test