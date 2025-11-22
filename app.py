import streamlit as st
import pandas as pd
import pickle 

dbfile=open('salary.pickle','rb')
model=pickle.load(dbfile)


st.title("Salary prediction")
age = st.number_input("Enter your age",18,60)
exp=st.number_input("Enter your experience:",0,40)
gender=st.radio("Gender",["Male","Female"])
education=st.selectbox("Education",["Bachelor's","Master's","PhD"])
if st.button("Prediction"):
	if gender=="Male":
		gender=True
	else:
		gender=False

	if education=="Bachelor's":
		b=1;m=0;p=0
	elif education=="Master's":
		b=0;m=1;p=0
	else:
		b=0;m=0;p=1


df=pd.DataFrame({
	"Age":[age],
	"Years of Experience":[exp],
	"Male":[gender],
	"Bachelor's":[b],
	"Master's":[m],
	"PhD":[p]})

st.dataframe(df)
result=round(model.predict(df)[0][0],2)
st.write(result)
st.write("success")
print(result)
st.balloons()
st.snow()
