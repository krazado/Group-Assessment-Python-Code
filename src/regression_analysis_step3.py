import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import datareader as dr

df = dr.read_data()

# Assuming your data has features X and target variable y
# Exlude SAT from regression
X = df[['MAN', 'TYP', 'INCOME']]
y = df['REV']

# Fit the linear regression model
X = sm.add_constant(X)  # Add a constant term for the intercept
model = sm.OLS(y, X).fit()

# Extract coefficients, standard errors, t-values, p-values, and confidence intervals
coefficients = model.params
std_errors = model.bse
t_values = model.tvalues
p_values = model.pvalues
conf_ints = model.conf_int()  # 95% confidence intervals by default

# Round all values to two decimal places
coefficients = coefficients.round(2)
std_errors = std_errors.round(2)
t_values = t_values.round(2)
p_values = p_values.round(2)
conf_ints = np.round(conf_ints, 2)

# Create row titles
row_titles = ['Intercept'] + X.columns.drop('const').tolist()

# Combine the statistics into a DataFrame
summary_df = pd.DataFrame({
    'Coefficient': coefficients,
    'Standard Error': std_errors,
    't-value': t_values,
    'p-value': p_values,
    '95% Confidence Interval': [f'({conf_ints.iloc[i][0]}, {conf_ints.iloc[i][1]})' for i in range(len(conf_ints))]
})

# Regression statistics
regression_stats = {
    'R Square': round(model.rsquared_adj, 2),
    'Adjusted R Square': round(model.rsquared_adj, 2),  # Include Adjusted R Square
    'Standard Error': round(np.sqrt(model.mse_resid), 2),
    'Observations': model.nobs
}

# Create a DataFrame for regression statistics
regression_stats_df = pd.DataFrame.from_dict(regression_stats, orient='index', columns=['Regression Statistic'])

# Plot the summary tables
fig, axes = plt.subplots(2, 1, figsize=(8, 6))

# Add Regression Statistics table
table1 = axes[0].table(cellText=regression_stats_df.values,
                       colLabels=regression_stats_df.columns,
                       rowLabels=regression_stats_df.index,
                       cellLoc='center',
                       loc='upper left',
                       colWidths=[0.5],
                       cellColours=[['lightgrey'] * len(regression_stats_df.columns)] * len(regression_stats_df.index))

table1.auto_set_font_size(False)
table1.set_fontsize(8)
table1.scale(1.2, 1.2)
axes[0].axis('off')

# Create a matrix to store cell colors
colors = np.where(summary_df['p-value'] > 0.05, 'red', 'white')

# Add the summary table with cell colors
table2 = axes[1].table(cellText=summary_df.values,
                       colLabels=summary_df.columns,
                       rowLabels=row_titles,
                       cellLoc='center',
                       loc='center',
                       colWidths=[0.2, 0.2, 0.2, 0.2, 0.4],
                       cellColours=[['white', 'white', 'white', color, 'white'] for color in colors])

table2.auto_set_font_size(False)
table2.set_fontsize(8)
table2.scale(1.2, 1.2)
axes[1].axis('off')

plt.tight_layout()
plt.show()
