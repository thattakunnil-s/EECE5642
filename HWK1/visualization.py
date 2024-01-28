import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('C:/Users/steff/OneDrive/Documents/Masters/Sem 4/Data Visualization/Assignments/Hwk1/heart_2020.csv')

# Visualization 1: Pie Chart
heart_disease_counts = data['HeartDisease'].value_counts()
plt.figure(figsize=(8, 5))
plt.pie(heart_disease_counts, labels=heart_disease_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Individuals with and without Heart Disease')
plt.axis('equal')
plt.show()

# Visualization 2: Faceted Line Plot
age_order = ['18-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80 or older']
data['AgeCategory'] = pd.Categorical(data['AgeCategory'], categories=age_order, ordered=True)

g = sns.FacetGrid(data, col="HeartDisease", height=5, aspect=1)
g.map(sns.lineplot, "AgeCategory", "BMI", ci=None)
g.set_xticklabels(rotation=45)
g.set_axis_labels('Age Category', 'Average BMI')
g.add_legend()
plt.subplots_adjust(top=0.9)
g.fig.suptitle('BMI by Age - Heart Disease Status')
plt.show()

# Visualization 3: Bar Chart
diabetic_data = data[data['Diabetic'] == 'Yes']

plt.figure(figsize=(8, 5))
sns.countplot(x='Smoking', hue='HeartDisease', data=diabetic_data, palette='Set1')
plt.title('Heart Disease in Diabetic Individuals - Smoking Status')
plt.xlabel('Smoking Status')
plt.ylabel('Count')
plt.legend(title='Heart Disease')
plt.show()
