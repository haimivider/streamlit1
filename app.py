import pandas as pd
import os
import streamlit as st
#from pydrive.auth import GoogleAuth
#from pydrive.drive import GoogleDrive

#gauth = GoogleAuth()
#drive = GoogleDrive(gauth)

money_first_day = 750000

# Add a title and intro text
st.title('Summary results by year')
st.text('This is a web app to allow watching our stocks return results')

upload_file = st.file_uploader('Upload a file of the requested year:')

if upload_file is not None:
   st.write(upload_file.name[:4])
   # If it has then do the following:

   # Read the file to a dataframe using pandas
   df = pd.read_csv(upload_file)
   df['return_for_specific_trancision'] = df['return'] * df['amount_money']
   #st.write(df['return_for_specific_trancision'])

   bruto_return, neto_return, commissions = st.columns(3)

   with bruto_return:
       st.markdown("**Bruto_return (in %)**")
       number1 = round(((int(df['return_for_specific_trancision'].sum())) / money_first_day), 2)
       st.markdown(f"<h1 style='text-align: left;font-size: 30px; color: red;'>{number1} {'%'}</h1>", unsafe_allow_html=True)

   with neto_return:
       st.markdown("**Neto_return (in %)**")
       number2 = round((((int(df['return_for_specific_trancision'].sum()) - int(df['commission'].sum())) / money_first_day)),2)
       st.markdown(f"<h1 style='text-align: left;font-size: 30px; color: red;'>{number2}{'%'}</h1>", unsafe_allow_html=True)

   with commissions:
       st.markdown("**Commissions (in $)**")
       number3 = int(df['commission'].sum())
       st.markdown(f"<h1 style='text-align: left;font-size: 30px; color: red;'>{number3}{'$'}</h1>", unsafe_allow_html=True)



   # Create a section for the dataframe statistics
   #st.header('Statistics of Dataframe')
   #st.write(df.describe())
