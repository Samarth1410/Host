import streamlit as st
import pickle
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from datetime import date

with open('https://github.com/Samarth1410/Host/raw/main/Shopkeepe', 'rb') as f:
    lr = pickle.load(f)

pred_val=lr.predict(start=247,end=247+30)

ls = []

for i in range(0, len(pred_val), 7):
    ls.append(pred_val[i:i+7].mean())

rng = pd.date_range(date.today(), periods=len(ls), freq='w')
pred_df = pd.DataFrame({ 'Date': rng, 'Val': ls }) 
print(pred_df)

# pred_df.to_csv('Shopkeeper.csv')
# import sys
# print(sys.executable)
# print(pd.python__version__)