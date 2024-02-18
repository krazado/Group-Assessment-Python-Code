import matplotlib.pyplot as plt
import datareader as dr


df = dr.read_data_com()

# Sample data for four scatter plots
x1 = df['COM']
y1 = df['REV']

x2 = df['COM2']
y2 = y1

x3 = df['Log(COM)']
y3 = y1

x4 = df['1/COM']
y4 = y1

# Create four subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Plot data on each subplot
axs[0, 0].scatter(x1, y1)
axs[0, 0].set_title('Default - COM')

axs[0, 1].scatter(x2, y2)
axs[0, 1].set_title('COM2')

axs[1, 0].scatter(x3, y3)
axs[1, 0].set_title('Log(COM)')

axs[1, 1].scatter(x4, y4)
axs[1, 1].set_title('1/COM')

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()