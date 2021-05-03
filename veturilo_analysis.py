# %%
import pandas as pd
# %%
df = pd.read_csv('veturilo_statistics.csv')
# %%
df.describe()
# %%
df.head(5)
# %%
df['date']=pd.to_datetime(date_column, infer_datetime_format = True)
# %%
df['day']=df['date'].apply(lambda x: x.day)
df['month']=df['date'].apply(lambda x: x.month)
df['year']=df['date'].apply(lambda x: x.year)
df['hour']=df['date'].apply(lambda x: x.hour)
df['minute']=df['date'].apply(lambda x: x.minute)
# %%
df = df.drop(columns='date')
# %%
df.head()
# %%
df['bike_numbers']=df['bike_numbers'].fillna(0)
# %%
def number_of_bikes(s):
    return s.count(',')+1
# %%
df.dtypes
# %%
df.bike_numbers.isnull().sum()
# %%
