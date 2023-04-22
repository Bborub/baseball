

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

df=pd.read_csv('baseball.csv')

df.head()
