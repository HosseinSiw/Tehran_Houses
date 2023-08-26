import streamlit as st
import joblib
import pandas as pd
import numpy as np
from utils import addresses

model = joblib.load('Pipe_Line.joblib')
st.title('Calculating Cost of homes in Tehran using Artificial Intelligence')
Address = st.selectbox(
    'Select your desired area',
    addresses,
)
Area = (st.text_input('What is the size of the house in question? (only number of the size, eg : 80)'))
Room = st.slider('How many Rooms do you want?', min_value=0, max_value=6)

Parking_input = st.toggle('Parking?',)
Warehouse_input = st.toggle('Warehouse?',)
Elevator_input = st.toggle('Elevator?',)


parking, elevator, warehouse = 0, 0, 0
if Parking_input:
    parking = 1
if Elevator_input:
    elevator = 1
if Warehouse_input:
    warehouse = 1


def pred():
    data = np.array([Area, Room, parking, elevator, warehouse, Address])
    res = int(model.predict(data))
    format_res = '{:,}'.format(res)
    return st.success(f'Estimated Price: {format_res} Toman')


st.write('Author: Hossein Siadati')
st.button('Predict', on_click=pred)
st.write('I have considered the dollar price constant 30,000$')
