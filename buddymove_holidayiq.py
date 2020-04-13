import pandas as pd

df = pd.read_csv('/home/jack/Desktop/buddymove_holidayiq.csv')

df.describe

from sqlalchemy import create_engine
engine = create_engine('sqlite://', echo=False)

df.to_sql('review', con=engine, if_exists='replace',index_label = 'Id')

print('\nbuddymove_holidayiq (from df to sql)\n')

result = engine.execute("SELECT COUNT(*) FROM review ").fetchone()
print('Length of new table: ')
print(f'{result}\n')

# How many users who reviewed at least 100 Nature in the category 
# also reviewed at least 100 in the Shopping category?

result2 = engine.execute("SELECT COUNT(*) FROM review WHERE Nature >= 100 AND Shopping >= 100").fetchall()
print('Number of users who reviewed at least 100 in nature and shopping: ')
print(f'{result2}\n')

# (Stretch) What are the average number of reviews for each category?

result3 = engine.execute("SELECT AVG(Sports), AVG(Religious), AVG(Nature), AVG(Theatre), AVG(Shopping) ,AVG(Picnic) FROM review").fetchone()
print('Average number for reviews in each category:\n')
print(f'Sports: {result3[0]}, Religious: {result3[1]}, Nature: {result3[2]}, Theatre: {result3[3]}, Shopping: {result3[4]}, Picnic: {result3[5]}')