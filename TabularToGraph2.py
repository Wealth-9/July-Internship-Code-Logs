import pandas as pd
import numpy as np
import networkx as nx



#creating my own random dataset using pandas
np.random.seed(42) #for same output 

accounts = ["A","B","C","D","E"]

n_transactions = 10 # no of rows /transactions

df = pd.DataFrame({
    "sender":np.random.choice(accounts, n_transactions),
    "receiver":np.random.choice(accounts, n_transactions),
    "amount":np.random.randint(10,500, n_transactions)
})

print(df)
# Converting Tabular data to a graph.
G = nx.from_pandas_edgelist( #reads dataframe row by row and builds a graph
  df,
  source="sender", #the starting point/nodes
  target="receiver", #ending column/arrow head
  edge_attr="amount", # add attribute amountto edge data
  create_using=nx.DiGraph()  #a directed graph as money flows from sender to reciever if not NetworkX defaults to an undirected graph
 )

print("Nodes:",G.nodes())
print("Edges:", G.edges(data=True))