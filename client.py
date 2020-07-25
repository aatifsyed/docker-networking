# %% [markdown]
# Run this interactively

# %% Imports
import pandas as pd
import requests
import json
import pickle

# %% Utility variables
server: str = "http://server.aatif.net:44713"

with open("data/train.csv") as f:
    original: pd.DataFrame = pd.read_csv(f)

# %% Make a GET
get = requests.get(server)

# %% POST for JSON
post = requests.post(server, json={"min": 5, "max": 10, "fmt": "JSON"})
unjsoned: pd.DataFrame = pd.read_json(post.text)

# %% POST for pickle
post = requests.post(server, json={"min": 10, "max": None, "fmt": "pickle"})
unpickled: pd.DataFrame = pickle.loads(post.content)
