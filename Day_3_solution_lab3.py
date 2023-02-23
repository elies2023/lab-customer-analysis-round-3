#!/usr/bin/env python
# coding: utf-8

# ## Lab | Customer Analysis Round 2

# In[ ]:


# # For this lab, we will be using the marketing_customer_analysis.csv file that you can find in the files_for_lab folder. Check out the files_for_lab/about.md to get more information if you are using the Online Excel.

# Note: For the next labs we will be using the same data file. Please save the code, so that you can re-use it later in the labs following this lab.

# Dealing with the data
# Show the dataframe shape.
# Standardize header names.
# Which columns are numerical?
# Which columns are categorical?
# Check and deal with NaN values.
# Datetime format - Extract the months from the dataset and store in a separate column. Then filter the data to show only the information for the first quarter , ie. January, February and March. Hint: If data from March does not exist, consider only January and February.
# BONUS: Put all the previously mentioned data transformations into a function.


# In[229]:


import pandas as pd
import numpy as np


# In[230]:


df=pd.read_csv("./marketing_customer_analysis.csv")


# In[231]:


df


# In[232]:


df.shape


# In[233]:


df.head()


# In[234]:


df.tail()


# In[235]:


df.dtypes


# In[236]:


df=df.drop(df.columns[0], axis=1)
df


# In[237]:


df.columns


# In[238]:


df.columns=df.columns[:].str.lower()


# In[239]:


df.columns


# In[240]:


df=df.rename(columns={'customer lifetime value':'customer_lifetime_value',
       'effective to date':'effective_to_date','employmentstatus':'employment_status', 
       'location code':"location_code", 'marital status':"'marital_status'", 'monthly premium auto':'monthly_premium_auto',
       'months since last claim':'months_since_last_claim', 'months since policy inception':'months_since_policy_inception',
       'number of open complaints':'number_of_open_complaints', 'number of policies':'number_of_policies', 'policy type':'policy_type',
        'renew offer type':'renew_offer_type', 'sales channel':'sales_channel', 'total claim amount':'total_claim_amount',
       'vehicle class':'vehicle_class', 'vehicle size':'vehicle_size', 'vehicle type':'vehicle_type'})

df


# #Data Type

# In[241]:


df.select_dtypes(['int32','float64'])


# In[242]:


df.select_dtypes(['object'])


# In[243]:


# data types

df._get_numeric_data()


# In[244]:


df.select_dtypes('object')


# In[245]:


df.isna()


# In[246]:


#number of null value
df.isna().sum()


# In[247]:


#percentage of null_value
percentage_missing_value = (df.isnull().sum() / len(df)) * 100
percentage_missing_value


# In[248]:


# because of the number of values of vehicle_type is high so i decided to drop this column
df = df.drop(['vehicle_type'], axis=1)


# In[249]:


df


# In[254]:


# deal with null value of months_since_last_claim
#df['months_since_last_claim'].unique()
df['months_since_last_claim']=df['months_since_last_claim'].fillna(0)
display(df['months_since_last_claim'].unique())


# In[255]:


# deal with null value of 'number_of_open_complaints
df['number_of_open_complaints'].unique()


# In[272]:


df['number_of_open_complaints'].value_counts()


# In[261]:


df['number_of_open_complaints']=df['number_of_open_complaints'].fillna(0)
display(df['number_of_open_complaints'].unique())


# In[270]:


#deal with nan values columns vehicle class,size
df['vehicle_size'].unique()
df['vehicle_size']=df['vehicle_size'].fillna('unknown')
display(df['vehicle_size'].unique())


# In[271]:


df['vehicle_size'].value_counts()


# In[279]:


df['vehicle_class'].unique()


# In[284]:


df['vehicle_class']=df['vehicle_class'].fillna("unknown")
display(df['vehicle_class'].unique())


# In[285]:


#Dealing with null value of response
df['vehicle_class'].value_counts()


# In[293]:


df['response'].unique()
df['response']=df['response'].fillna('No')
display(df['response'].unique())


# In[294]:


df['response'].value_counts()


# In[299]:


#dealing with null value state  
df['state'].unique()
df['state'].value_counts()


# In[303]:


df['state']=df['state'].fillna("California ")
df['state'].unique()


# In[304]:


# cheking miss values
df.isna().sum()


# In[286]:


df['effective_to_date'] = pd.to_datetime(df['effective_to_date'], errors='coerce')
df.head()


# In[287]:


import time
from datetime import date


# In[288]:


df['month_column'] = df['effective_to_date'].dt.month
df


# In[289]:


first_quarter = [1, 2, 3]  # month values for the first quarter
df_first_quarter = df[df['effective_to_date'].dt.month.isin(first_quarter)]
df_first_quarter


# ## Lab | Customer Analysis Round 3

# In[159]:


# EDA (Exploratory Data Analysis) - Complete the following tasks to explore the data:
# Show DataFrame info.
# Describe DataFrame.
# Show a plot of the total number of responses.
# Show a plot of the response rate by the sales channel.
# Show a plot of the response rate by the total claim amount.
# Show a plot of the response rate by income.


# In[160]:


df.info


# In[161]:


df.describe()

#df.describe().T


# In[319]:


import matplotlib.pyplot as plt
import seaborn as sns 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[324]:


df['response_rate']=np.where(df['response'] =='No', 0 , 1)
df


# In[330]:


df['response_rate'].value_counts()


# In[335]:


#plot response_rate
df.response_rate.value_counts().plot.bar()
plt.show


# In[329]:


#plot response rate by sales_channel
sns.barplot(x='sales_channel', y='response_rate', data=df)
plt.title('Response Rate by Sales Channel')
plt.ylabel('Response Rate')
plt.show()


# In[336]:


Show a plot of the response rate by the total claim amount.
Show a plot of the response rate by income.


# In[339]:


#Show a plot of the response rate by the total claim amount.
df['total_claim_amount'].unique()


# In[341]:


#plot response rate by total claim amount
sns.barplot(x='total_claim_amount', y='response_rate', data=df)
plt.title('Response Rate by total claim value')
plt.ylabel('response_rate')
plt.show()


# In[342]:


sns.barplot(x='income', y='response_rate', data=df)
plt.title('Response Rate by total income')
plt.ylabel('response_rate')
plt.show()


# In[ ]:





# In[ ]:




