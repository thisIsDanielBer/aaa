import json
import requests
import pandas as pd

def characters_by_ep():
  query = """
query {
  characters{
    results{
      name
      episode{
        name
      }
    }
  }
}
"""
  url = r"https://rickandmortyapi.com/graphql"
  response = requests.post(url, json={'query': query})
  json_data = json.loads(response.text)

  df_data = json_data["data"]["characters"]["results"]
  df = pd.DataFrame(df_data)
  df.sort_values('episode',key=lambda x:x.str.len())    
  print(df)    
  
characters_by_ep()