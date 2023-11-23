import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Constants
NUM_SAMPLES = 100
NUM_VARIABLES = 2
FIGURE_SIZE = (12, 10)

# Set seed for reproducibility
np.random.seed(0)

# Generate random data
data = np.random.randn(NUM_SAMPLES, NUM_VARIABLES)

# Create subplots
fig, axes = plt.subplots(2, 2, figsize=FIGURE_SIZE)

# Bar chart for Mean and Median
a, b = data[:, 0], data[:, 1]
axes[0, 0].bar(['Mean', 'Median'], [np.mean(a), np.median(a)], label='Variable 1', color='blue', alpha=0.7)
axes[0, 0].bar(['Mean', 'Median'], [np.mean(b), np.median(b)], label='Variable 2', color='green', alpha=0.7)
axes[0, 0].legend(loc='upper right')
axes[0, 0].set_title('Descriptive Statistics: Mean and Median')

# Heatmap for correlation analysis
sns.heatmap(np.corrcoef(data.T), annot=True, ax=axes[0, 1], annot_kws={"size": 12}, cmap='coolwarm')
axes[0, 1].set_title('Correlation Analysis')

# Histograms of variables
axes[1, 0].hist(a, bins=15, label='Variable 1', color='blue', alpha=0.7)
axes[1, 0].hist(b, bins=15, label='Variable 2', color='green', alpha=0.7)
axes[1, 0].legend()
axes[1, 0].set_title('Histogram of Variables')
axes[1, 0].set_xlabel('Values')
axes[1, 0].set_ylabel('Frequency')

# Scatter plot
axes[1, 1].scatter(a, b, alpha=0.7)
axes[1, 1].set_xlabel('Variable 1')
axes[1, 1].set_ylabel('Variable 2')
axes[1, 1].set_title('Scatter Plot of Variable 1 vs Variable 2')

# General title for the entire figure
fig.suptitle('Exploratory Data Analysis')

# Adjust layout
plt.tight_layout()
plt.show()
print('Done')