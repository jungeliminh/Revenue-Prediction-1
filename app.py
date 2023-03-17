import pickle
import sklearn
import numpy as np

filename = 'model.pickle'

model = pickle.load(open(filename, "rb"))

import streamlit as st

st.title('Revenue Prediction')
temp = np.array(st.number_input('Input temperature:'))
temp_pred = model.predict(temp.reshape(-1, 1))
st.text('Revenue Prediction')
if st.button('Predict'):
  st.success(*temp_pred)
