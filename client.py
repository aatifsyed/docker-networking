# %% [markdown]
# Run this interactively

# %% Imports
import pandas as pd
import requests
import json

# %% Utility variables
server: str = "http://server.aatif.net:44713"

with open("data/train.csv") as f:
    db_df: pd.DataFrame = pd.read_csv(f)

# %% Make a GET
get = requests.get(server)

# %% Make a query
post = requests.post(server, json={"Minimum": 5, "Maximum": 10})
df: pd.DataFrame = pd.read_json(post.text)
