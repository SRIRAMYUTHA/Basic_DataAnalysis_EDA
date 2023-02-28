import streamlit as st
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image,ImageFilter,ImageEnhance


# Title and Subheader
st.title("Data Visualization")
st.subheader("Data Visualization using Streamlit ")

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")


DATA_PATH = os.path.join(dir_of_interest, "data", "titanic.csv")


df = pd.read_csv(DATA_PATH)
# st.dataframe(df)

# Age
if st.checkbox("Age"):
    fig, ax = plt.subplots()
    ax.hist(df['age'], bins=20)
    st.pyplot(fig)
# fare
if st.checkbox("Fare"):
    fig, ax = plt.subplots()
    ax.hist(df['fare'], bins=20)
    st.pyplot(fig)


    
	
    





	
	
	
	


