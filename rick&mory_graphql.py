import json
import requests
import pandas as pd

def characters_by_ep():
  query = """
query{
  characters{
    results {
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
  max = 0 
  character = ""
  for result in df_data:
    episodes = len(result["episode"])
    
    if episodes > max:
      max = episodes
      character = result["name"]
      
  print(character)
    
characters_by_ep()