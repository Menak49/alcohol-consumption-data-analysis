

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":
    df = pd.read_csv("data/merged.csv")
    sns.heatmap(df.corr(numeric_only=True),cmap="coolwarm")
    plt.show()

