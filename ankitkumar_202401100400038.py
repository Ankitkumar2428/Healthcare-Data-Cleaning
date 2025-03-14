# -*- coding: utf-8 -*-
"""Ankitkumar_202401100400038.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LzN8EO5zAINpl4kR11SOgRH0RGtN81Pl
"""

import pandas as pd

# Load dataset
df = pd.read_csv('/content/drive/MyDrive/heart_disease.csv')

"""**Handling Missing data**


"""

# Check missing values
print(df.isnull().sum())

df.head()
#revisiting data

"""GRAPH"""

import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(7, 5))

# Create a histogram with  for 'Heart Disease Status'
sns.histplot(
    x=df_u30['Age'],
    kde=True,
    hue=df_u30['Heart Disease Status'],
    palette='pastel'  # Changed color palette
)

# Add title and axis labels
plt.title("Age Distribution of Individuals ≤30")
plt.xlabel("Age")
plt.ylabel("Frequency")

# Display the plot
plt.show()

"""**Disease prediction**"""

plt.figure(figsize=(6, 6))

# Create a count plot for 'Gender' with hue for 'Heart Disease Status'
sns.countplot(
    x='Gender',
    hue='Heart Disease Status',
    data=df_u30,
    palette="Set2"  # Changed color palette
)

# Add title and axis labels
plt.title("Heart Disease Status by Gender (≤30)")
plt.xlabel("Gender")
plt.ylabel("Count")

# Display the plot
plt.show()

#Pridicting disease
sns.countplot(
    x='Smoking',
    hue='Heart Disease Status',
    data=df_u30,
    palette="Set2"
)

# Add title and axis labels
plt.title("Smoking vs Heart Disease Status (≤30)")
plt.xlabel("Smoking")
plt.ylabel("Count")

# Display the plot
plt.show()

sns.countplot(
    x='Exercise Habits',
    hue='Heart Disease Status',
    data=df_u30,
    palette="Set2"
)

# Add title and axis labels
plt.title("Exercise Habits vs Heart Disease Status (≤30)")
plt.xlabel("Exercise Habits")
plt.ylabel("Count")

# Display the plot
plt.show()

sns.boxplot(
    x='Heart Disease Status',
    y='BMI',
    data=df_u30,
    palette="Set1"
)

# Add title and axis labels
plt.title("BMI Distribution by Heart Disease Status (≤30)")
plt.xlabel("Heart Disease Status")
plt.ylabel("BMI")

# Display the plot
plt.show()