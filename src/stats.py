import pandas as pd
import matplotlib.pyplot as plt

from src import constants as const

def get_column_statistics(df, col):

    # Select only desired columns
    df_selected = df[col].apply(pd.to_numeric, errors='coerce')

    # Generate statistics 
    stats_df = df_selected.describe().T

    # Add IQR columns
    stats_df['IQR'] = stats_df['75%'] - stats_df['25%']

    # Add CV columns
    stats_df['CV'] = stats_df['std']/stats_df['mean']

    # Create figure
    fig, ax = plt.subplots(figsize=(12,6))
    ax.axis('off')

    # Create table
    table = ax.table(
        cellText=stats_df.round(3).values,
        colLabels=stats_df.columns,
        rowLabels=stats_df.index,
        loc='center'
    )

    # Customization
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1,1.5)

    for (row, col), cell in table.get_celld().items():
        
        # Columns headers
        if row == 0:
            cell.set_facecolor('#ADD8E6') 
            cell.set_text_props(weight='bold')

        # Row headers
        if col == -1:
            cell.set_facecolor('#ADD8E6') 
            cell.set_text_props(weight='bold')

    # Save figure
    plt.savefig(f'{const.OUTPUT_FILE}stats_table',bbox_inches = 'tight', dpi=300)
    plt.close()

    return stats_df