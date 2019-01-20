# coding: utf-8

# In[1]:
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:
df = pd.read_csv(r'E:\datasets\fifa19\data.csv', sep=',')
df


# In[3]:
len(set(df.Nationality))


# In[4]:
dict_with_countries = dict()
for country in set(df.Nationality):
    dict_with_countries[country] = len(df[df.Nationality == country])

dict_with_countries    


# In[5]:
dict_with_countries = {country : value 
                       for country, value in dict_with_countries.items() 
                       if value > 400}
dict_with_countries


# In[6]:
#Команду ниже используем только в Jupyter Notebook
#%matplotlib inline
plt.style.use('ggplot')

labels = dict_with_countries.keys()
values = dict_with_countries.values()

plt.xlabel('Country')
plt.ylabel('Num of players')

plt.xticks(range(0, 10), labels, rotation='vertical')

plt.bar(labels, values, 0.5, color='#d62728')

#Эту команду используем, если мы не пользуемся Jupyter Notebook
plt.figure().clear()


# In[7]:
df.columns.values


# In[8]:
positions = [pos 
             for pos in df.columns.values 
             if len(pos) <= 3]
positions.remove('ID')
positions.remove('Age')
positions


# In[31]:
min_age = df.Age.min()
max_age = df.Age.max()

min_age, max_age


# In[9]:
ages = range(16, 46)
dict_with_ages = dict()

for age in set(df.Age):
    dict_with_ages[age] = len(df[df.Age == age])
    
dict_with_ages    


# In[10]:
labels = dict_with_ages.keys()
values = dict_with_ages.values()

plt.xticks(range(2, 31), 
           [str(a) for a in labels], 
           rotation='vertical')

plt.xlabel('Age')
plt.ylabel('Num of players')

plt.bar(range(2, 31), 
        values, 
        color='blue', 
        width=.75)
        
#Эту команду используем, если мы не пользуемся Jupyter Notebook
plt.figure().clear()     


# In[11]:
dict_with_rating = dict()
for rating in set(df.Overall):
    dict_with_rating[rating] = len(df[df.Overall == rating])
    
dict_with_rating    


# In[12]:
labels = dict_with_rating.keys()
values = dict_with_rating.values()

plt.xticks(range(0, 49), 
           [str(a) for a in labels], 
           rotation='vertical')

plt.xlabel('Rating')
plt.ylabel('Num of players')

plt.bar(range(0, 48), 
        values, 
        color='green', 
        width=.75)
        
#Эту команду используем, если мы не пользуемся Jupyter Notebook
plt.figure().clear()     


# In[13]:
df.Overall.mean()


# In[14]:
clubs = ['Liverpool', 
         'FC Barcelona', 
         'Juventus',
         'Paris Saint-Germain',
         'Chelsea', 
         'Real Madrid', 
         'FC Bayern München']

dict_with_players_in_clubs = dict()

for club in clubs:
    dict_with_players_in_clubs[club] = len(df[df.Club == club])
    
dict_with_players_in_clubs    


# In[15]:
dict_with_mean_rating_in_clubs = dict()

for club in clubs:
    dict_with_mean_rating_in_clubs[club] = int(df.Overall[df.Club == club].mean())
    
dict_with_mean_rating_in_clubs  


# In[16]:
dict_with_mean_age_in_clubs = dict()

for club in clubs:
    dict_with_mean_age_in_clubs[club] = int(df.Age[df.Club == club].mean())
    
dict_with_mean_age_in_clubs


# In[17]:
labels = dict_with_players_in_clubs.keys()
values = dict_with_players_in_clubs.values()

plt.xticks(range(0, 7), 
           labels, 
           rotation='vertical')

plt.xlabel('Club')
plt.ylabel('Num of players')

plt.bar(range(0, 7), 
        values, 
        color='#D2691E', 
        width=.75)
        
#Эту команду используем, если мы не пользуемся Jupyter Notebook
plt.figure().clear()     


# In[18]:
labels = dict_with_mean_rating_in_clubs.keys()
values = dict_with_mean_rating_in_clubs.values()

plt.xticks(range(0, 7), 
           labels, 
           rotation='vertical')

plt.xlabel('Club')
plt.ylabel('Mean rating')

plt.bar(range(0, 7), 
        values, 
        color='#FF0000', 
        width=.75)
        
#Эту команду используем, если мы не пользуемся Jupyter Notebook
plt.figure().clear()        


# In[19]:
labels = dict_with_mean_age_in_clubs.keys()
values = dict_with_mean_age_in_clubs.values()

plt.xticks(range(0, 7), 
           labels, 
           rotation='vertical')

plt.xlabel('Club')
plt.ylabel('Mean age')

plt.bar(range(0, 7), 
        values, 
        color='#00FFFF', 
        width=.75)
 
#Используем при запуске не через Jupyter 
plt.show()        
