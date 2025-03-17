import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('Zomatodataset/zomato.csv',encoding="latin-1")
print(df.shape)

##now from here we are performing the data checks using eda
##now in data analysis the main thing we have to do is::
#finding the missing values
#finding duplicates 
#finding numerical and categorical values
#finding the relationship between the features
df.isnull().sum()#so here we will get all the features and it checks how many null values are there for specific feature

#another way

null_val=[features for features in df.columns if df[features].isnull().sum()>0]
print(null_val)


#finding the missing values