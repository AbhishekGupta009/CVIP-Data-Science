#!/usr/bin/env python
# coding: utf-8

# In[36]:


import pandas as pd
import numpy as np


# In[5]:


df =pd.read_csv(r"C:\Users\user\Desktop\globalterrorism.csv",encoding='ISO-8859-1')


# In[6]:


df.head()


# In[7]:


df.shape


# In[8]:


df.columns


# In[9]:


df.rename(columns={'eventid':'EID','iyear':'Year','imonth':'Month','iday':'Day','approxdate':'Approxdate','extended':'Extend','country_txt':'Country','provstate':'state',
                       'region_txt':'Region','attacktype1_txt':'AttackType','target1':'Target','nkill':'Killed',
                       'nwound':'Wounded','summary':'Summary','gname':'Group','targtype1_txt':'Target_type',
                       'weaptype1_txt':'Weapon_type','motive':'Motive'},inplace=True)


# In[10]:


df=df[['Year','Month','Day','Country','state','Region','city','latitude','longitude','AttackType','Killed',
               'Wounded','Target','Summary','Group','Target_type','Weapon_type','Motive']]


# In[11]:


df.isnull().sum()


# In[12]:


df.head()


# In[13]:


print("Nation with the most assaults : ",df['Country'].value_counts().idxmax())
print("The most-attacked city : ",df['city'].value_counts().index[1])
print("Area with the most assaults:",df['Region'].value_counts().idxmax())
print("The most attacks-per-year:",df['Year'].value_counts().idxmax())
print("Attacks per month peak:",df['Month'].value_counts().idxmax())
print("With the most assaults as a group:",df['Group'].value_counts().index[1])
print("Attacks of Most Types:",df['AttackType'].value_counts().idxmax())


# In[14]:


df['Year'].value_counts(dropna=False).sort_index()


# In[15]:


df[['Killed', 'Wounded']] = df[['Killed', 'Wounded']].fillna(df[['Killed', 'Wounded']].mean())
df[['Killed','Wounded']].isnull().any()


# In[16]:


df = df.dropna(subset=['Summary'])
df = df.dropna(subset=['Motive'])


# In[17]:


df[['Summary','Motive']].isna().any()


# In[18]:


df['Day'].unique()


# In[19]:


df['Day'] = df['Day'].replace(0,np.nan)
df = df.dropna(subset=['Day'])

# Checking no. of unique values in Day Column
print(df['Day'].nunique())

# Checking for null values
print(df['Day'].isnull().any())


# In[21]:


df.isnull().sum()


# In[22]:


df.reset_index(inplace=True,drop=True)
df.head()


# In[24]:


df.info()


# In[25]:


df_cat = df.select_dtypes(include=['object']).columns.tolist()
df_cat


# In[27]:


df_num = df.select_dtypes(exclude=['object']).columns.tolist()
df_num


# In[28]:


df.describe()


# In[29]:


df.describe(include='O')


# In[55]:


import matplotlib.pyplot as plt
df.hist(figsize=(10,10))
plt.show()


# In[54]:


import seaborn as sns
plt.figure(figsize=(15,5))
sns.countplot(x = df['Year'])
plt.title('Terrorist Activities per Year')
plt.xlabel('Attacking Years')
plt.ylabel('No. of Attacks per Years')
plt.xticks(rotation=90)
plt.show()


# In[39]:


kill_per_year = df[['Year','Killed']].groupby('Year').sum()
kill_per_year.plot(kind='bar', figsize=(15,5), title = 'No. of People Killed Per Year')
plt.xlabel('Attacking Years')
plt.ylabel('No.of Peoples Killed ')
plt.show()


# In[41]:


wounded_per_year = df[['Year','Wounded']].groupby('Year').sum()
wounded_per_year.plot(kind='bar', figsize=(15,5), title = 'No. of People Wounded Per Year')
plt.xlabel('Attacking Years')
plt.ylabel('No.of Peoples Wounded')
plt.show()


# In[44]:


plt.figure(figsize=(15,10))
most_attack_countries = df['state'].value_counts().head(10)
most_attack_countries.plot(kind='pie',autopct = '%.2f%%')
plt.title('Top 10 Mostly Attacked States')
plt.xlabel('States')
plt.ylabel(None)
plt.show()


# In[46]:


df['Target'].value_counts()


# In[47]:


plt.figure(figsize=(10,5))
most_target_peoples = df['Target'].value_counts().head(10)
most_target_peoples.plot(kind='bar')
plt.title('Most Target Peoples by Terrorists Attacks')
plt.xlabel('Most Target Peoples')
plt.ylabel('No. of Terrorists Attacks')
plt.xticks(rotation=45)
plt.show()


# In[48]:


terr_groups = df['Group'].value_counts()
terr_groups


# In[50]:


targets = df['Target_type'].value_counts()
targets


# In[51]:


fig = plt.figure(figsize=(15,6))
sns.barplot(x = targets.index, y = targets.values)
plt.title("Most frequent target types of terrorists")
plt.xlabel("Targets")
plt.ylabel("Number of Terrorist Attacks")
plt.xticks(rotation=90)
plt.show()


# In[53]:


sns.heatmap(df.corr(),annot=True,cmap='viridis')
plt.show()


# In[ ]:




