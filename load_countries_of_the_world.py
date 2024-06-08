import psycopg2
import pandas as pd

con = psycopg2.connect(
  database="fced_catarina_rocha",             # your database is the same as your username
  user="fced_catarina_rocha",                 # your username
  password="ROCHA",                          # your password
  host="dbm.fe.up.pt",                      # the database host
  port="5433",
  options='-c search_path=project2'     # use the schema you want to connect to
)

cur = con.cursor()
cur.execute(f'DELETE FROM happiness')
cur.execute(f'DELETE FROM country')


countries = pd.read_csv('data/countries of the world.csv', decimal=',')
countries['Country'] = countries['Country'].str[:-1]
cols = ['Country', 'Population', 'Area (sq. mi.)', 'Infant mortality (per 1000 births)', 'GDP ($ per capita)', 'Literacy (%)', 'Region', 'Climate']

countries = countries[cols]
records = countries.values.tolist()

sql_insert = '''
  INSERT INTO country (country_name, population, area, infant_mortality, gdp, literacy, region, climate) 
  VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
  '''

print(countries.loc[223])
cur.executemany(sql_insert, records[:223])  # Western Sahara produces error...
cur.executemany(sql_insert, records[224:])
con.commit()


