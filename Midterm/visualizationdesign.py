import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Input data into a DataFrame
data = {
    "Department": ["Distribution", "Facilities", "Human Resources", "Information Systems"],
    "Q1 Budget": [390000, 675000, 350000, 950000],
    "Q1 Actual": [375000, 693000, 346000, 925000],
    "Q2 Budget": [395000, 800000, 350000, 850000],
    "Q2 Actual": [382000, 837000, 342000, 890000],
    "Q3 Budget": [400000, 750000, 350000, 875000],
    "Q3 Actual": [390000, 713000, 340000, 976000],
    "Q4 Budget": [410000, 750000, 350000, 900000],
    "Q4 Actual": [408000, 790000, 367000, 930000]}

df = pd.DataFrame(data)

# Calculating the deviation percentage
for i in range(1, 5):
    df[f'Q{i} Deviation (%)'] = ((df[f'Q{i} Actual'] - df[f'Q{i} Budget']) / df[f'Q{i} Budget']) * 100

# Setting up the bar graph
fig, ax = plt.subplots(figsize=(14, 7))
width = 0.2
x = np.arange(len(df))  # label locations

# Plotting the deviation as a bar graph
for i in range(1, 5):
    ax.bar(x + width*(i-2.5), df[f'Q{i} Deviation (%)'], width, label=f'Q{i}')

ax.set_ylabel('Deviation (%)')
ax.set_title('Percentage Deviation of Actual Expenses from Budget by Department and Quarter')
ax.set_xticks(x)
ax.set_xticklabels(df["Department"])
ax.legend()
ax.yaxis.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Setting up the line graph
fig, ax = plt.subplots(figsize=(14, 7))
colors = ['b', 'g', 'r', 'c']  # Colors for the lines

# Plotting the deviation as a line graph
for i, color in zip(range(1, 5), colors):
    ax.plot(df["Department"], df[f'Q{i} Deviation (%)'], color=color, marker='o', linestyle='-', label=f'Q{i}')

ax.set_ylabel('Deviation (%)')
ax.set_title('Trend of Percentage Deviation of Actual Expenses from Budget by Department')
ax.set_xticks(np.arange(len(df["Department"])))
ax.set_xticklabels(df["Department"])
ax.legend()
ax.yaxis.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
