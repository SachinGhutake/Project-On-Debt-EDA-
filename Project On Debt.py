#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv(r"C:\Users\Lenovo\Downloads\CS_Training.csv")
data


# In[3]:


data.drop("Unnamed: 0",axis=1 , inplace = True)


# In[4]:


data.info()


# # Cleaning

# In[5]:


# 1. Tell which column has null values


# In[6]:


data.isnull().sum()


# In[7]:


# 2. For any column fill the missing value with a mean value


# In[8]:


a = data.mean()
a


# In[9]:


data = data.fillna(a)
data


# In[10]:


data.isnull().sum()


# In[11]:


# 3 . RevolvingUtilizationOfUnsecuredLine column: No Missing Value And Filter Values only b/w 0 And 1


# In[12]:


data = data[data['RevolvingUtilizationOfUnsecuredLines'].between(0,1)]
data


# In[13]:


# Cap the age column b/w 18 and 80


# In[14]:


data = data[data['age'].between(18,80)]
data


# In[15]:


# take the column DebtRatio above 1


# In[16]:


data = data[data['DebtRatio'] > 1]
data


# In[17]:


# For column, NumberOfOpenCreditLinesAndLoans take a value less than 30


# In[18]:


data = data[data['NumberOfOpenCreditLinesAndLoans'] < 30]
data


# In[19]:


# For column MonthlyIncome cap it b/w 1000 and 50000


# In[20]:


data = data[data['MonthlyIncome'].between(1000,50000)]
data


# In[21]:


# For column NumberRealEstateLoansOrLines cap it less than 6


# In[22]:


data = data[data['NumberRealEstateLoansOrLines'] < 6]
data


# In[23]:


# For column NumberOfDependents cap it b/w 0 and 5


# In[24]:


data = data[data['NumberOfDependents'].between(0,5)]
data


# # Visualization

# In[25]:


# For each column try to visualize with an appropriate visual(mostly a distribution plot)


# In[26]:


data.plot(x="SeriousDlqin2yrs", y=["RevolvingUtilizationOfUnsecuredLines"], kind='hist',bins=8,color='yellow',figsize=(10,8))
plt.title('Revolving Of Unsecured Lines ')
plt.grid(which='major', axis='both')
plt.show()


# In[27]:


data.plot(x="SeriousDlqin2yrs", y=["DebtRatio","MonthlyIncome"], kind='line',figsize=(10,8))
plt.title('SeriousDlqin2yrs Wise DebtRatio AND MonthlyIncome')
plt.grid(which='major', axis='both')


# In[28]:


data.plot(x="SeriousDlqin2yrs", y=["NumberOfOpenCreditLinesAndLoans","NumberRealEstateLoansOrLines"], kind='hist',figsize=(10,8))
plt.title('SeriousDlqin2yrs Wise CreditLines Loans AND RealEstateLines Loans')
plt.grid(which='major', axis='both')
plt.show()


# In[29]:


plt.figure(figsize=(15,8))
data.plot.scatter(x= 'NumberOfTime30-59DaysPastDueNotWorse',y= 'NumberOfTime60-89DaysPastDueNotWorse',color='hotpink',
                   s=12, alpha=0.5)
plt.title('Number Of Past Due 30-59 TO 60-89 Days')
plt.xlabel('Number Of Past Due 30-59 Days')
plt.ylabel('Number Of Past Due 60-89 Days')
plt.show()


# In[30]:


plt.figure(figsize=(12,8))
plt.hist(data['age'], bins=10,color='yellow')
plt.hist(data['NumberOfDependents'], bins=7,color='red')
plt.title('Distribution of Age & Number Of Dependents')
plt.legend(['age','Number Of Dependents'])
plt.show()


# # EDA

# In[31]:


# Tell us the distribution(%) of value in the column NumberRealEstateLoansOrLines


# In[32]:


distribution  = data['NumberRealEstateLoansOrLines'].value_counts(normalize=True).reset_index()
distribution 


# In[33]:


# From the Distribution plot can you tell me for each column, which distribution is normal or which is not


# In[34]:


# From The Distribution Plot We Can Say That 'NumberOfOpenCreditLinesAndLoans' and 'NumberRealEstateLoansOrLines' is normal
# because The Plots Are Exactly On An Left Side Or The Middle,and Some Are In The Right Side It Shows This Will Be The Normal,
# And The Others Are Mostly Lie On '0th' Position Means That To Left Side Therfore That Will Be Not Proper Distributed.


# In[35]:


# Create new column NOCLL_Cat from NumberOfOpenCreditLinesAndLoans by :


# In[36]:


def fn_1(row):
    if row['NumberOfOpenCreditLinesAndLoans'] < 5:
        return 1
    elif row['NumberOfOpenCreditLinesAndLoans'] <=5 and row['NumberOfOpenCreditLinesAndLoans'] < 8:
        return 2
    elif row['NumberOfOpenCreditLinesAndLoans'] <=8 and row['NumberOfOpenCreditLinesAndLoans'] < 11:
        return 3
    else:
        return 4
 
data['NOCLL_Cat'] = data.apply(lambda row: fn_1(row),axis=1)


# In[37]:


b= data[['NumberOfOpenCreditLinesAndLoans','NOCLL_Cat']].head()
b


# In[38]:


# Visualize NOCLL_Cat as bar graph distribution


# In[39]:


bar_graph =sns.displot(data.NOCLL_Cat, kde=True, rug=True)
bar_graph


# In[40]:


# Average MonthlyIncome, NumberOfDependent wise where age is greater than 30


# In[41]:


age = data[data['age']> 30]
Average = age.groupby(['NumberOfDependents'])['MonthlyIncome'].mean().reset_index()
Average


# In[42]:


# Average DebtRatio, where MonthlyIncome is less than 10000


# In[43]:


a = round(data.loc[data['MonthlyIncome'] < 10000]['DebtRatio'].mean(),2)
a


# In[ ]:




