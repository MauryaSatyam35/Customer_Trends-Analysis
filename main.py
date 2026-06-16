import pandas as pd
df = pd.read_csv('Customer Trend Analysis.csv')

print(df.head())
print(df.info())
print(df.describe(include='all'))
print(df.isnull().sum())
df['Review Rating']=df.groupby('Category')['Review Rating'].transform(lambda x:x.fillna(x.median()))
print(df.isnull().sum())
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ', '_')
print(df.columns)
df=df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})
print(df.columns)
# To Create s new coloumn age_group
labels = ['Adult','Young Adult','Middle-Aged','Senior' ]
df['age_group']=pd.qcut(df['age'],q=4,labels=labels)
print(df[['age','age_group']].head(20))
# create a column purchase_frequency_days
frequency_mapping ={
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Daily': 1,
    'Annually': 365,
    'Every 3Month': 90,
    'Quarterly': 4,
}
df['purchase_frequency_days']=df['frequency_of_purchases'].map(frequency_mapping)
df[['purchase_frequency_days','frequency_of_purchases']].head(20)
print(df[['purchase_frequency_days','frequency_of_purchases']].head(10))
print(df[['discount_applied','promo_code_used']].head(10))
print(df['discount_applied'].shape)
print(df['promo_code_used'].shape)
print(df['discount_applied'].unique())
print(df['promo_code_used'].unique())
print(df.columns.tolist())
df['discount_applied']=df['discount_applied'].fillna('No')
df['promo_code_used']=df['promo_code_used'].fillna('No')
print(df['discount_applied'].unique())
print(df['promo_code_used'].unique())
df=df.drop('promo_code_used',axis=1)
print(df.columns)
# step 1:  connect to postgreSQL
# Replace placeholder with Actual Details

from sqlalchemy import create_engine
from urllib.parse import quote_plus
username="postgres"
password= quote_plus("M@uryaji1204")
host="localhost"
port="5432"
database="customer_trends"

engine = create_engine(f"postgresql://{username}:{password}@{host}:{port}/{database}")
# step2 Load dataframe in postregsql
table_name = "customer"
df.to_sql(table_name, engine, if_exists='replace', index=False)
print(f"data successfully uploaded to {table_name}'in database'{database}'.")
