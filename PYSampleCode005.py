# Import the necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

# Define a variable N
N = 500

# Construct the colormap
current_palette = sns.color_palette("muted", n_colors=5)
cmap = ListedColormap(sns.color_palette(current_palette).as_hex())

# Initialize the data
data1 = np.random.randn(N)
data2 = np.random.randn(N)
# Assume that there are 5 possible labels
colors = np.random.randint(0,5,N)

# Create a scatter plot
plt.scatter(data1, data2, c = colors, cmap = cmap)

# Add a color bar
plt.colorbar()

# Show the plot
plt.show()

