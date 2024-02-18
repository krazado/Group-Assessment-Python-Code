import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from matplotlib.gridspec import GridSpec
import datareader as dr

df = dr.read_data()

# Compute the correlation matrix
correlation_matrix = df.corr()

# Create a mask to hide the upper triangle
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))

# Set the diagonal of the mask to False
mask[np.diag_indices_from(mask)] = False

# Assuming your data has features X and target variable y
X = df[['MAN', 'TYP', 'INCOME','COM','STA']] 
y = df['REV'] 

# Create a GridSpec to adjust the layout
fig = plt.figure(figsize=(12, 6))
gs = GridSpec(1, 2, width_ratios=[3, 1])

# Plot the correlation matrix
ax0 = plt.subplot(gs[0])
sns.heatmap(correlation_matrix, mask=mask, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5, ax=ax0)
ax0.set_title('Correlation Matrix')

plt.show()
