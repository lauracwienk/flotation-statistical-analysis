# Imports 
from src import histogram, remove_outliers
from src import constants as const

import pandas as pd

if __name__ == "__main__":
    # Read Excel file
    df = pd.read_csv(const.CSV_FILE, decimal=',') 

    # Columns to plot
    columns = [
        '% Iron Feed', 
        '% Silica Feed', 
        'Starch Flow',
        'Amina Flow',
        'Ore Pulp Flow',
        'Ore Pulp pH',
        'Ore Pulp Density',
        '% Iron Concentrate',
        '% Silica Concentrate'
    ]  
    print(df[columns])

    # Generate new histograms
    #histogram.histogram(df, columns, 'Histograma para dados brutos de:', 'hist') 

    # Remove outliers routine
    # df_modified = remove_outliers.remove_outliers(df, columns)
    # #print(df_modified)

    # # Save in a new excel File
    # #df_modified.to_excel('flotation_wot_outliers.xlsx', index=False)

    # # Generate new histograms
    # histogram.histogram(df_modified, columns, 'Histograma após remoção de outliers:', 'hist_wot_outliers')