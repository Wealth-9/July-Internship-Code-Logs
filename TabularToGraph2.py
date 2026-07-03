import pandas as pd
import numpy as np

np.random.seed(42) #for same output 

accounts = ["A","B","C","D","E"]

n_transactions = 10 # no of rows /transactions

df = pd.DataFrame({
    "sender":np.random.choice(accounts, n_transactions),
    "receiver":np.random.choice(accounts, n_transactions),
    "amount":np.random.randint(10,500, n_transactions)
})

print(df)