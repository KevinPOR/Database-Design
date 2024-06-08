import psycopg2
import pandas as pd
import sys

#print (sys.argv[1])
#print (sys.argv[2])  # use year as input argument
years = [2015, 2016,2017,2018,2019]

con = psycopg2.connect(
  database="fced_catarina_rocha",             # your database is the same as your username
  user="fced_catarina_rocha",                 # your username
  password="ROCHA",                       # your password
  host="dbm.fe.up.pt",                      # the database host
  port="5433",
  options='-c search_path=project2'     # use the schema you want to connect to
)


records = []
for year in years:
    cur = con.cursor()
    cur.execute(f'DELETE FROM happiness')
    
    happiness = pd.read_csv('wh-'+str(year)+'_new.csv', decimal=',')
    cols = ['Happiness Rank','Country', 'Happiness Score']
    
    happiness = happiness[cols]
    string_list = happiness['Happiness Rank']

    happiness['Happiness Rank'] = [int(float(i)) for i in happiness['Happiness Rank']]
    
    
    happiness.reset_index(inplace=True)
    happiness['year'] = year
    print(happiness)
    
    rec = happiness.values.tolist()
    records=[*records,*rec]
    
c=1
for sub in records:
    sub.insert(0,c)
    sub.pop(1)
    c+=1
    
sql_insert = '''
  INSERT INTO happiness (ref, rank, country_name, happiness_score,year) 
  VALUES (%s,%s, %s, %s,%s)
  '''
  
  
print(records)
cur.executemany(sql_insert, records)
con.commit()


