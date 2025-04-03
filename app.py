#pip install streamlit
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Hello World')
st.header('This is a header')
st.subheader('This is a subheader')
st.write("Today we are learingn Streamlit")
st.button('Submit', type="primary")
st.button("Submit", type="secondary")
st.button("Submit", type="tertiary")
# st.checkbox("Male", value=True)
df=st.checkbox("Male", value=True)
if df==True:
    st.write(f"I am male")
else:
    st.write(f"I am male")

st.radio("fruits", ["apple", "banana", "orange"])


st.text_input("Enter your name", placeholder="Type here", max_chars=10)

st.text_area("Enter your thoughts", placeholder="YOur opinion here", max_chars=50, height=150)

st.number_input("year", min_value=2000, max_value=2050, step=2, placeholder="Increasing year", value=2023)


# st.slider("Select a range", min_value=0, max_value=100, step=5)

num=st.slider("Select a range", min_value=0, max_value=100, step=5)

st.write(f"Selected number is {num}")

data=st.file_uploader("Upload a file", type=["csv", "txt"])

if data:
    df=pd.read_csv(data)
    st.dataframe(df)

y=np.linspace(0, 10, 100)
x=np.sin(y)

fig,ax=plt.subplots()
ax.plot(y, x)
st.pyplot(fig)