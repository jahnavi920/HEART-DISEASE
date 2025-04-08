import streamlit as st
import joblib
clf=joblib.load("heart disease.joblib")
st.title("HEART DISEASE PRDICTION")
a=st.number_input("Enter age")
c=st.number_input("Enter number of cgs per day")
tc=st.number_input("Enter number of colestrol ")
sbp=st.number_input("Enter sysBP")
dbp=st.number_input("Enter disbp")
bmi=st.number_input("Enter BMI")
hr=st.number_input("Enter heart rate")
g=st.number_input("Enter glucose")
if st.button("predict"):
    prediction=clf.predict([[a,c,tc,sbp,dbp,bmi,hr,g]])
    if prediction==0:
        st.text("No chance for heart disease")
    else:
        st.text("You might have a heart disease")
