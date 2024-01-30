import streamlit as st 
#import os
#import sqlite3
import tensorflow as tf 
import numpy as np 
import keras as K 
import streamlit as st 

def login():

    ids = {'Kevin' : 'TCL123' ,'Kate' : 'TCL456'}
    

    st.title('Login Page')
    with st.form(key='login_form'):

        username = st.text_input('Enter Username',value = '', key='username')
        password = st.text_input('Enter Password',value = '',key='password')

        sumbit_button = st.form_submit_button('Login')
        if sumbit_button:
            if username in ids.keys():
                if password == ids[username]:
                    #st.switch_page('pages/recommender_page.py')
                    session_state = st.session_state
                    session_state.logged_in = True
                    st.experimental_rerun()
                else : st.error('Invalid password')
            else : st.error('Invalid username')


def run_app():

    model = K.models.load_model('recommender.h5')

    Course = st.text_input(label='Course',value ='', key ='Course')
    GPA = st.number_input(label='GPA', key='GPA')
    Affordability = st.text_input(label ='Affordability',value='', key='Affordability')
    Region = st.number_input(label='Region', key ='Region')
    evaluation = ''

    course_idx = {'Medical': 1,'Engineering' : 2,'Science' :3}
    affordability_idx = {'Class A': 1,'Class B' : 2, 'Class C': 3 }
    

    

    if st.button('Evaluation'):

        
        
        try: 
            Course = course_idx[Course]
            Affordability = affordability_idx[Affordability]
            inp = tf.constant([[Course,GPA,Affordability,Region]])
            output = model.predict(inp)[0][0]

            if output < 0.5 :
                evaluation = 'Private'
            else:
                evaluation = 'State'
        
        except Exception as e:
            st.write('Please enter the correct values')
        
    
    st.write('Our Suggestion')
    st.markdown(f'<div style="background-color:lightgreen; padding:15px">{evaluation}', unsafe_allow_html=True)


if __name__ == '__main__':

    if not hasattr(st.session_state, 'logged_in') or not st.session_state.logged_in:
        login()
    else:
        run_app()


