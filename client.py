# %% [markdown]
# Run this interactively

# %% Imports
import pandas as pd
import requests
import json

# %% Utility variables
server: str = "http://server.aatif.net:44713"

# %% Make a get
r = requests.get(server)
