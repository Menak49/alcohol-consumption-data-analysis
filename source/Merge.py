import pandas as pd

if __name__ == "__main__":
    mat = pd.read_csv("data/student-mat.csv")
    por = pd.read_csv("data/student-por.csv")

    # 
    identity_cols = [
        "school", "sex", "age", "address", "famsize", "Pstatus",
        "Medu", "Fedu", "Mjob", "Fjob", "reason", "guardian",
        "traveltime", "studytime", 
        "schoolsup", "famsup", "activities", "nursery",
        "higher", "internet", "romantic",
        "famrel", "freetime", "goout", "Dalc", "Walc",
        "health"
    ]

    #

    merged = pd.merge(
        mat, por,
        how='outer',  
        on=identity_cols,
        suffixes=('_mat', '_por')
    )

    print(merged.dtypes)


    # Nominal (catégories non ordonnées)
    nominal_cols = [
        "school", "sex", "address", "famsize", "Pstatus",
        "Mjob", "Fjob", "reason", "guardian", "nursery",
        "higher", "internet", "romantic",
        "schoolsup", "famsup", "activities",
        "paid_mat", "paid_por"
    ]

    for col in nominal_cols:
        if col in merged.columns:
            merged[col] = merged[col].astype("category")

    # Ordinal
    edu_type = pd.CategoricalDtype(categories=[0, 1, 2, 3, 4], ordered=True)
    travel_study_type = pd.CategoricalDtype(categories=[1, 2, 3, 4], ordered=True)
    failures_type = pd.CategoricalDtype(categories=[0, 1, 2, 3], ordered=True)
    likert_5_type = pd.CategoricalDtype(categories=[1, 2, 3, 4, 5], ordered=True)

    ordinal_map = {
        edu_type: ["Medu", "Fedu"],
        travel_study_type: ["traveltime", "studytime"],
        failures_type: ["failures"],
        likert_5_type: ["famrel", "freetime", "goout", "Dalc", "Walc", "health"],
    }

    for dtype, cols in ordinal_map.items():
        for col in cols:
            if col in merged.columns:
                merged[col] = merged[col].astype(dtype)

    merged.to_csv("data/merged.csv", index=False)
    print(merged.dtypes)
    