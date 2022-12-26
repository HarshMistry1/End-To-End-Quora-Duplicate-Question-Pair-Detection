import streamlit as st
import helper
import pickle

model = pickle.load(open('ran_for_model.pkl','rb'))

st.header('Duplicate Question Pairs')

q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    query = helper.query_point_creator(q1,q2)
    result = model.predict(query)[0]

    if result:
        st.warning('Duplicate')
    else:
        st.success('Not Duplicate')