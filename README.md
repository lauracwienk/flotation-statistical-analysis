This repository is dedicated to treat flotation data from the following 
dataset: https://www.kaggle.com/datasets/edumagalhaes/quality-prediction-in-a-mining-process

**How to activate python virtual environment and used libraries**
| Step | Command | Description |
|-------|---------|-----------|
| 1 | `python -m venv venv` | Create virtual environment |
| 2 | `source venv/Scripts/activate` | Activate virtual environment (Linux/Mac) |
| 2b | `venv\Scripts\activate` | Activate virtual environment in Windows CMD |
| 3 | `pip install -r requirements.txt` | Install packages from file `requirements.txt` |

**The following statistics treatment were performed in the dataset:**

1. Set all data in the same timestamp (Since we have some columns sampled every 20 seconds and others sampled on a hourly base, we've set all data in hourly base, taking averages for 20 seconds collected variables).
2. Select the following variables to be analysed: % Iron Feed, % Silica Feed, Starch Flow, Amina Flow, Ore Pulp Flo, Ore Pulp pH, Ore Pulp Density, % Iron Concentrate, % Silica Concentrate.
3. Plot histogram and boxplot graphics to analyse raw data behaviours.
4. Remove outliers from raw data based on IQR rule.
5. Plot histogram and boxplot graphics to analyse treated data behaviours.
6. Get data statistical measures (median, average, standard deviation, etc.) to help characterize dataset 
7. Get linear and non-linear correlations (pearson and spearman) and define most important variables to affect the following targets:
% Fe Concentrate and % Si concentrate. In this step, heatmap and scatterplot are also plotted to help visualization data behaviours. 


**Main conclusions**
1. % Si Concentrate has the biggest CV value (47.7%), which indicates high variability of values in comparison to the others 
variables. In terms of process control, this can be related to pH fluctuation, pulp feed instability or amine dosage instability. 
2. Amina Flow also has a significant value for CV (16.7%), which can contribute to % Si Concentrate high variability result. 
3. Other sign of % Si Concentrate high variability is mean (2.308) and median (1.99) differences. When we check histogram and boxplot 
plots too, it is possible to see this variability as well. 
4. By contrast, % Fe Feed has mean (56.295) and median (56.08) values with smaller difference, as a result of its lower variability (CV = 0.092).