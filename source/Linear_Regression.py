
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OrdinalEncoder
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


# sklearn preprocessing label encoder     :     lamsize (Label encoder) pour passer du binaire au numérique  comprendre ce que ça fait




if __name__ == "__main__":

    file_mat = '../data/student-mat.csv'
    file_por = '../data/student-por.csv'
    mat = pd.read_csv(file_mat)
    por = pd.read_csv(file_por)
    print(mat.head())
    print(mat.shape)
    print(por.head())
    print(por.shape)
    print('ee')


    scaler = StandardScaler
    X_scaled = mat



    # # joined = mat.join(por, on = ["school","sex","age","address","Medu","Fedu","nursery","internet"])
    # # print(joined.head())
    
    
    # Regression linéaire sur les données pour estimer l'age


    all_cols = ["school","sex","address","Medu","Fedu","nursery","internet", 'G1', 'G2','age', 'absences', 'goout', 'Dalc']
    cols_bin = ["school", "sex", "address", "nursery", "internet"]
    estimated_col = 'G3'

    oe = OrdinalEncoder()  # Permet d'encoder les variables binaires en 0 1 on peut aussi utiliser labelencoder : peut aussi encoder avec un ordre pour les var qualitatives ordinales
    mat[cols_bin] = oe.fit_transform(mat[cols_bin])
    print( mat[cols_bin])
    # Construction XTrain/Ytrain :
    XTrain_sdf = mat[all_cols]
    XTrain = XTrain_sdf
    YTrain_sdf = mat[[estimated_col]]
    YTrain = YTrain_sdf

    # Apprentissage model lineaire :
    from sklearn import linear_model
    reg_model = linear_model.LinearRegression()
    reg_model.fit(XTrain, YTrain)

    # Estimation des valeurs manquantes/atypiques :
    df = mat.copy(deep = 'yes')
    indexToPredict = df[df['age']%2 == 0].index
    print(indexToPredict)
    XToPredict = df.loc[indexToPredict, all_cols]
    print(XToPredict)
    YAgeEstim = reg_model.predict(XToPredict)
    df[estimated_col] = df[estimated_col].astype(float) 
    df.loc[indexToPredict, estimated_col] = YAgeEstim
    
    df_comp = 2*(abs(df['age'] - mat['age']))/mat['age']

    print(df_comp.mean()*100) # Erreur en %

    y_reel = mat[mat['age']%2 == 0][estimated_col]
    y_predit = df.loc[indexToPredict][estimated_col]

    print(y_reel)
    print(y_predit)
    plt.scatter(y_reel, y_predit, alpha=0.5)
    plt.plot([y_reel.min(), y_reel.max()],
            [y_reel.min(), y_reel.max()],
            'r--', linewidth=1)   # droite idéale y = x
    plt.xlabel("Valeurs réelles")
    plt.ylabel("Valeurs prédites")
    plt.title(f"{estimated_col} : Prédites vs réelles")
    plt.show()





