import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'C:/Users/steff/OneDrive/Documents/Masters/Sem 4/Data Visualization/Assignments/Hwk2/data-1.xlsx'
data = pd.read_excel(file_path)

# Correcting any potential whitespace issues in column names
data.columns = [col.strip() for col in data.columns]

# Extracting conference name from the 'Conference (Name'Year)' column
data['Conference'] = data['Conference (Name\'Year)'].apply(lambda x: x.split("'")[0].strip())

# Grouping by Conference and calculating the aggregated values
conference_grouped_data = data.groupby('Conference').agg(
    Average_Acceptance_Rate = ('Acceptance rate', lambda x: round(x.mean()*100, 2)),
    Total_Accepted_Papers = ('Num. of accepted papers', 'sum'),
    Total_Submissions = ('Num. of total submissions', 'sum')).reset_index()

# Creating a table visualization for the aggregated data
fig_table, ax_table = plt.subplots()
ax_table.axis('tight')
ax_table.axis('off')
table = ax_table.table(cellText=conference_grouped_data.values,
                       colLabels=["Conference Name", "Average Acceptance Rate (%)", "Total Accepted Papers", "Total Submissions"],
                       loc='center')
plt.title('Conference Data Over Years')

# Creating a graph visualization for CVPR
cvpr_data = data[data['Conference (Name\'Year)'].str.contains('CVPR')].copy()
cvpr_data['Year'] = cvpr_data['Conference (Name\'Year)'].apply(lambda x: x.split("'")[1]).astype(int)
cvpr_data.sort_values(by='Year', inplace=True)

# Plotting the graph
fig_graph, ax_graph = plt.subplots()
ax_graph.plot(cvpr_data['Year'], cvpr_data['Acceptance rate'], marker='o')
ax_graph.set_title('CVPR Acceptance Rate Over Years')
ax_graph.set_xlabel('Year')
ax_graph.set_ylabel('Acceptance Rate')

plt.show()
