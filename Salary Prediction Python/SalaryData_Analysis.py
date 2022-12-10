# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 14:23:51 2022

@author: ___
"""

# %%
# import packages
import sklearn
from sklearn.metrics import mean_absolute_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import missingno as msn
import pandas as pd
import matplotlib.pyplot as plt  # plotting
import seaborn as sns  # plotting


# %%

# import dataset
data = pd.read_csv("SalaryData.csv")
# if using on another computer, modify the above line or put this code in same folder as data.
# read head
data.head()

# %%
'''
SUMMARY STATISTICS
'''
# %%

# describe
data.describe().transpose()
# %%

# columns in the data
data.columns
# %%
'''
'Employee ID', 'Age', 'Education', 'Gender', 'Project Involvement',
'Job Level', 'Job Role', 'Salary', 'Over 18 years old',
'Total Working Years', 'Years At Company', 'Years In Current Role'
'''
# %%

# check the distribution of Job Role in the data
pd.value_counts(data['Job Role']).plot(
    kind='bar').set_title('Distribution of the Job Role')
# %%

# check the distribution of Gender in the data
pd.value_counts(data['Gender']).plot(
    kind='bar').set_title('Distribution of gender')
# %%

# check the distribution of Over 18 years old in the data
pd.value_counts(data['Over 18 years old']).plot(kind='bar')

# it seems that there are all observations for all Over 18 years old
# %%

'''
DATA PRE-PROCESSING AND CLEANING
'''
# %%

# check missing observations
# install if missing as:
# pip install missingno

# if using anaconda distribution then:
# conda install missingno

# check missing observations now
msn.bar(data)

# it seems that there are no missing observations.
# the data is clean and now we can begin feature extraction
# %%

# Label encoding

'''
The following variables need label encoding (changing from class string
to class factor and then numeric categorical variables):
    - Gender
    - Job Level
We can verify this by running the dtypes function.

The Over 18 years old variable will be dropped since it has no impact on analysis.
'''
data.dtypes
# %%

# label_encoder object knows how to understand word labels.
# and convert them into numeric labels.
label_encoder = preprocessing.LabelEncoder()

# %%
data['Gender'] = label_encoder.fit_transform(data['Gender'])
data['Job Role'] = label_encoder.fit_transform(data['Job Role'])

# drop the 'Over 18 years old' variable
data = data.drop(['Over 18 years old', 'Employee ID'], axis=1)
# %%

'''
MODELLING
'''

'''
Looking at the data, the best variable to predict is salary, given the other explanatory variables.
Thus, our Y variable is 'Salary'.
'''


# correlation analysis
plt.figure(figsize=(10, 8))
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap=plt.cm.Blues)

'''
we drop all those variables with a correlation less than +/-0.15 with the "Salary" variable.
These variables are: Education, Gender, Project Involvement, and Job Role.
'''
# %%

data = data.drop(
    ['Education', 'Gender', 'Project Involvement', 'Job Role'], axis=1)

# %%
data.head()

# %%

sns.scatterplot(data=data, x="Age", y="Salary")

# %%
sns.scatterplot(data=data, x="Job Level", y="Salary")
# %%

sns.scatterplot(data=data, x="Total Working Years", y="Salary")
# %%
sns.scatterplot(data=data, x="Years At Company", y="Salary")
# %%
sns.scatterplot(data=data, x="Years In Current Role", y="Salary")

# %%
'''
From the above plots, nothing important can be revealed, but generally a positive relationship can be identified.
Modelling can now begin
'''


data.head()

# %%
# features set:
X = data.iloc[:, [0, 1, 3, 4, 5]]

# target:
Y = data.iloc[:, 2]
# %%

# splitting package
# spliting
# split ratio 0.8/0.2 and random seed number=42

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42)

# %%
'''Regression (MLR)'''
# import regression package

# instantiate
regress = LinearRegression()


# fit
regress.fit(X_train, Y_train)


Y_predict = regress.predict(X_test)
# %%

regression_score = regress.score(X_test, Y_test)
print('The regression model has an accuracy of ',
      round(regression_score*100, 2), '%')

# 92.28% accuracy

# %%

print('The model looks like:\n',
      'Salary = ', round(regress.intercept_, 2), '+',
      round(regress.coef_[0], 2), '(Age) + ',
      round(regress.coef_[1], 2), '(Job Level) +',
      round(regress.coef_[2], 2), '(Total Working Years) + ',
      round(regress.coef_[3], 2), '(Years At Company)',
      round(regress.coef_[4], 2), '(Years In Current Role)')
# %%
'''
The model looks like:
 Salary =  -2045.14 + 5.52 (Age) +  3696.1 (Job Level) + 64.37 (Total Working Years) +  7.86 (Years At Company) - 42.16 (Years In Current Role)
 '''

# %%
# getting the MAE

# MAE
mean_absolute_error(Y_test, Y_predict)

# mae = 1017.41
# this statistic is better interpreted anc useful if we use it to compare the current model with other models.
# %%

# saving predicted salary in the test data set
Predicted_Salary = Y_predict
X_test['Predicted Salary'] = Predicted_Salary
# %%
# saving the actual sales in the test data set
X_test['Actual Salary'] = Y_test
# %%

# exporting the fitted data
data_fitted = X_test

data_fitted.to_csv('SalesData_PredictedSales.csv')

# %%

# get user input to get prediction

print("Variables to predict your Salary are:\n Age, Job Level, Total Working Years, Years At Company, and Years In Current Role")
# %%

age = float(input('Enter your Age in Years: '))

job_level = float(input('Enter your Job Level: '))


total_w_yrs = float(input('Enter your Total Working Years: '))


yrs_at_co = float(input('Enter your Years at the Company: '))


yrs_in_role = float(input('Enter your Years in the Current Role: '))


Salary = regress.intercept_ + (regress.coef_[0]*age) + (regress.coef_[1]*job_level)+(
    regress.coef_[2]*total_w_yrs)+(regress.coef_[3]*yrs_at_co)+(regress.coef_[4]*yrs_in_role)


print('Your salary should be approximately:', round(Salary, 2))
# %%
