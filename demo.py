import requests
import pandas as pd
import sqlalchemy as db

#pulls ID for 500 top stories
response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty")
topStories = response.json()
df = pd.DataFrame.from_dict(topStories)
#print(df)
engine = db.create_engine('sqlite:///stories.db')
df.to_sql('topStories', con=engine, if_exists='replace', index=False)
with engine.connect() as connection:
   query_result = connection.execute(db.text("SELECT * FROM topStories;")).fetchall()
   print(pd.DataFrame(query_result))