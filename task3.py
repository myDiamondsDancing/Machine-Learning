# coding: utf-8

# In[80]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[81]:


df = pd.read_csv(r'C:\Python for beginners\who-suicide-statistics\who_suicide_statistics.csv', sep=',')
df


# In[82]:


usa = df[df.country == 'United States of America']
usa


# In[83]:


years = dict()

for i in range(1979, 2016):
    years[i] = usa[usa.year == i]

years    


# In[84]:


x_data = list(range(1979, 2016))

y_data = [sum(years[i].population) for i in years]  
y_data


# In[86]:


#For Jupyter
#matplotlib inline

plt.xlabel('year')
plt.ylabel('population')
plt.bar(x_data, y_data, align='center', color='green')

plt.savefig(r'C:\Python for beginners\ML\1.png', format='png')


# In[87]:


y_data = [sum(years[i].suicides_no) for i in years]

plt.xlabel('year')
plt.ylabel('suicides')
plt.title('Suicides in USA')
plt.bar(x_data, y_data, align='center', color='green')

plt.savefig(r'C:\Python for beginners\ML\2.png', format='png')


# In[67]:


age_categories = set(years[1979].age)
age_categories


# In[92]:


y_data = list()
for age_category in age_categories:
    suicides_num = 0
    for year in years:
        suicides_num += sum(years[year][years[year].age == age_category].suicides_no)
    y_data.append(suicides_num)
    
len(y_data)    


# In[94]:


x_data = list(age_categories)

ax = plt.figure().add_subplot(111)
        
x_axis = range(len(x_data))
        
ax.set_xticks(x_axis)
ax.set_title('Suicides by different ages')
ax.set_xlabel('age')
ax.set_ylabel('suicides')
ax.set_xticklabels(x_data, rotation=20)

ax.bar(x_data, y_data, align='center', color='red')

plt.savefig(r'C:\Python for beginners\ML\3.png', format='png')


# In[77]:


y_data = [sum(years[year].suicides_no) for year in years]
y_data


# In[95]:


men_data = [sum(years[year][years[year].sex == 'male'].suicides_no) for year in range(2000, 2010)]

women_data = [sum(years[year][years[year].sex == 'female'].suicides_no) for year in range(2000, 2010)] 


N = 10

ind = np.arange(2000, 2010)  
width = 0.35      

_, ax = plt.subplots()

men_bar = ax.bar(ind, men_data, width, color='r')

women_bar = ax.bar(ind + width, women_data, width, color='y')

ax.set_ylabel('Suicides')
ax.set_title('Suicides gender')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(ind)

ax.legend((men_bar[0], women_bar[0]), ('Men suicides', 'Women suicides'))

plt.savefig(r'C:\Python for beginners\ML\3.png', format='png')


# In[96]:


len(set(df.country))

# Not for Jupyter
plt.show()
