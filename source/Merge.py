import pandas as pd




if __name__ == "__main__":
    mat = pd.read_csv("data/student-mat.csv")
    por = pd.read_csv("data/student-por.csv")
    # print(mat.columns)
    # print(por.columns)

    # merge
    identity_cols = [
        "school", "sex", "age", "address", "famsize", "Pstatus",
        "Medu", "Fedu", "Mjob", "Fjob", "reason", "guardian",
        "nursery", "internet", "romantic", "famrel", "freetime",
        "goout", "Dalc", "Walc", "health", "higher","traveltime", "studytime",
    ]

    subject_cols = [
         "failures", "schoolsup", "famsup",
        "paid", "activities", "absences", "G1", "G2", "G3"
    ]

    merged = pd.merge(
        mat, por,
        how='outer',
        on=identity_cols,
        suffixes=('_mat', '_por')
    )

    # print(len(merged.drop_duplicates()))
    # print(merged.columns)
    # print(len(merged.columns))
    # print(merged.head())
    print(merged.dtypes)

    # types
    nominal_cols = [
    "school", "sex", "address", "famsize", "Pstatus",
    "Mjob", "Fjob", "reason", "guardian", "nursery",
    "higher", "internet", "romantic",
    "schoolsup_mat", "famsup_mat", "paid_mat", "activities_mat",
    "schoolsup_por", "famsup_por", "paid_por", "activities_por"
    ]
    for col in nominal_cols:
        merged[col] = merged[col].astype("category")

    edu_type      = pd.CategoricalDtype(categories=[0, 1, 2, 3, 4], ordered=True)
    travel_study_type = pd.CategoricalDtype(categories=[1, 2, 3, 4], ordered=True)
    failures_type = pd.CategoricalDtype(categories=[0, 1, 2, 3], ordered=True)
    likert_5_type = pd.CategoricalDtype(categories=[1, 2, 3, 4, 5], ordered=True)

    ordinal_map = {
        edu_type:         ["Medu", "Fedu"],
        travel_study_type: ["traveltime", "studytime"],
        failures_type:    ["failures_mat", "failures_por"],
        likert_5_type:    ["famrel", "freetime", "goout", "Dalc", "Walc", "health"],
    }
    for dtype, cols in ordinal_map.items():
        for col in cols:
            merged[col] = merged[col].astype(dtype)

    merged.to_csv("data/merged.csv", index=False)
    print(merged.dtypes)




