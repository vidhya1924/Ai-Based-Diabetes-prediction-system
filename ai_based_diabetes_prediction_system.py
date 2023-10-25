# -*- coding: utf-8 -*-
"""AI-Based Diabetes Prediction System

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xx8sla5TmDaagIMlelGa5Fg84FNG84TA
"""

import warnings
warnings.filterwarnings('ignore')

import numpy as np    # Importing the NumPy library for linear algebra operations
import pandas as pd   # Importing the Pandas library for data processing and CSV file handling

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

import seaborn as sns                   # Importing the Seaborn library for statistical data visualization
import matplotlib.pyplot as plt         # Importing the Matplotlib library for creating plots and visualizations
import plotly.express as px             # Importing the Plotly Express library for interactive visualizations

from google.colab import files
uploaded= files.upload()

df=pd.read_csv('diabetes (1).csv')

df.head(10)

df.tail(10)

df.dtypes

df.info()

print("No. of Zero Values in Glucose ", df[df['Glucose']==0].shape[0])

df['BloodPressure']=df['BloodPressure'].replace(0, df['BloodPressure'].mean())
df['SkinThickness']=df['SkinThickness'].replace(0, df['SkinThickness'].mean())
df['Insulin']=df['Insulin'].replace(0, df['Insulin'].mean())
df['BMI']=df['BMI'].replace(0, df['BMI'].mean())

df.describe()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming 'df' is your DataFrame containing the dataset
# If you haven't imported your dataset yet, import it here

# Create subplots
f, ax = plt.subplots(1, 2, figsize=(10, 5))

# Pie chart for Outcome distribution
df['Outcome'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
ax[0].set_title('Outcome')
ax[0].set_ylabel(' ')

# Count plot for Outcome distribution
sns.countplot(x='Outcome', data=df, ax=ax[1])  # Use 'x' instead of 'Outcome'
ax[1].set_title('Outcome')

# Display class distribution
N, P = df['Outcome'].value_counts()
print('Negative (0):', N)
print('Positive (1):', P)

# Adding grid and showing plots
plt.grid()
plt.show()

df.hist(bins=10, figsize=(10, 10))
plt.show()

plt.figure(figsize=(12, 6))
sns.heatmap(df.corr(), annot=True, cmap='Reds')
plt.plot()

target_name='Outcome'

y=df[target_name]

X= df.drop(target_name, axis=1)

X.head()

y.head()

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X)
SSX = scaler.transform(X)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(SSX, y, test_size=0.2, random_state=7)

X_train.shape, y_train.shape

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(solver='liblinear', multi_class='ovr')
lr.fit(X_train, y_train)

from sklearn.tree import DecisionTreeClassifier
dt=DecisionTreeClassifier()
dt.fit(X_train, y_train)