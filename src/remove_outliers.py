import pandas as pd


def remove_outliers(df, cols):
    df_cleaned = df.copy()
    mask = pd.Series(True, index=df.index)  

    for col in cols:
        df_cleaned[col] = pd.to_numeric(df_cleaned[col], errors='coerce')

        Q1 = df_cleaned[col].quantile(0.25)
        Q3 = df_cleaned[col].quantile(0.75)
        IQR = Q3 - Q1
        lsl = Q1 - 1.5 * IQR
        usl = Q3 + 1.5 * IQR

        mask &= df_cleaned[col].between(lsl, usl)
        
    df_cleaned = df_cleaned[mask]
    return df_cleaned