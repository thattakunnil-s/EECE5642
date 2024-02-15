import matplotlib.pyplot as plt
import numpy as np

# Product names
products = [
    "SCSI II Disk Drives 10 GB",
    "SCSI II Disk Drives 20 GB",
    "SCSI II Disk Drives 30 GB",
    "SCSI II Disk Drives 40 GB",
    "EISA Disk Drives 10 GB",
    "EISA Disk Drives 20 GB",
    "EISA Disk Drives 30 GB",
    "EISA Disk Drives 40 GB",
    "Removable Disk Drives 10 GB",
    "Removable Disk Drives 20 GB",
    "Removable Disk Drives 30 GB",
    "Removable Disk Drives 40 GB"]

# Quarter names
quarters = ['Q1', 'Q2', 'Q3', 'Q4']

# Simulate sales data
np.random.seed(0)
sample_sales_data = np.random.randint(100000, 1000000, (12, 4))

# Generate the line chart for the sales data
plt.style.use('ggplot')
fig, ax = plt.subplots(figsize=(14, 8))

# Colors for the lines
colors = plt.cm.viridis(np.linspace(0, 1, len(products)))

# Plotting a line for each product's sales data across the quarters
for i, product in enumerate(products):
    ax.plot(quarters, sample_sales_data[i], marker='o', label=product, color=colors[i])

# Add labels and title
ax.set_xlabel('Quarters')
ax.set_ylabel('Sales Revenue ($)')
ax.set_yticks(np.linspace(0, 1000000, 11))
ax.set_yticklabels(['${:,.0f}'.format(x) for x in np.linspace(0, 1000000, 11)])
ax.set_title('Sales Revenue by Product Across Four Quarters')

# Place a legend outside the plot
plt.subplots_adjust(right=0.75, top= 0.75)
ax.legend(title="Products", bbox_to_anchor=(1.05, 1), loc='center left')

# Show the plot
plt.show()
