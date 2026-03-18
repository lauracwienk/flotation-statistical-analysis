import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from src import constants as const

def histogram(
        df, 
        df_columns,
        title,
        path
):
    sns.set(style="whitegrid")  

    # Generate histograms
    for col in df_columns:
        # Convert df data into numeric type
        df[col] = pd.to_numeric(df[col], errors='coerce')

        plt.figure(figsize=(8, 5))

        # Plot histogram removing NaN values
        sns.histplot(df[col].dropna(), bins=20, kde=True, color='skyblue')
        plt.title(f'{title} {col}')
        plt.xlabel(col)
        plt.ylabel('Frequência')
        plt.tight_layout()
        
        # Save figure
        filename = os.path.join(const.OUTPUT_FILE, f'{path}_{str(col)}.png')
        plt.savefig(filename)
        plt.close()  