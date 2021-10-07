import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Import data
import pandas as pd
midwest = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/midwest_filter.csv")

# Plot
fig = plt.figure(figsize=(14, 9), dpi= 80, facecolor='w', edgecolor='k')    
colors = plt.cm.tab20.colors
categories = np.unique(midwest['category'])
for i, category in enumerate(categories):
    plt.scatter('area', 'poptotal', data=midwest.loc[midwest.category==category, :], s='dot_size', c=colors[i], label=str(category), edgecolors='black', linewidths=.5)

# Legend for size of points
for dot_size in [100, 300, 1000]:
    plt.scatter([], [], c='k', alpha=0.5, s=dot_size, label=str(dot_size) + ' TotalPop')
plt.legend(loc='upper right', scatterpoints=1, frameon=False, labelspacing=2, title='Saravana Stores', fontsize=8)
plt.title("Bubble Plot of PopTotal vs Area\n(color: 'category' - a categorical column in midwest)", fontsize=18)
plt.xlabel('Area', fontsize=16)
plt.ylabel('Poptotal', fontsize=16)
plt.show()     