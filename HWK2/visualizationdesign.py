import matplotlib.pyplot as plt

# Data for the bar chart
years = ['2009', '2019']
percentages = [77, 65]

# Create a bar chart with matplotlib
plt.figure(figsize=(10, 8))
bars = plt.bar(years, percentages, color='blue')

# Set the y-axis to start at 0 and end at 100%
plt.ylim(0, 100)

# Adding the data labels on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1, f'{yval}%', ha='center', va='bottom')

# Labeling Axes
plt.xlabel('Year')
plt.ylabel('Percentage (%)')

# Title of the bar chart
plt.title('Percentage of Americans that Identify as Christians')

# Display the plot
plt.show()
