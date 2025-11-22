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
gender_option = st.selectbox("Gender", ["Male", "Female"])
gender = 1 if gender_option == "Male" else 0

b_option = st.checkbox("Bachelor's")
b = 1 if b_option else 0

m_option = st.checkbox("Master's")
m = 1 if m_option else 0

p_option = st.checkbox("PhD")
p = 1 if p_option else 0

df = pd.DataFrame({
    "Age": [age],
    "Years of Experience": [exp],
    "Male": [gender],
    "Bachelor's": [b],
    "Master's": [m],
    "PhD": [p]
})

if st.button("Predict Salary"):
    pred = model.predict(df)

    # FIX: convert prediction (numpy array) → float
    result = round(float(pred), 2)

    st.success(f"Predicted Salary: {result}")
    st.balloons()
    st.snow()




# df=pd.DataFrame({
# 	"Age":[age],
# 	"Years of Experience":[exp],
# 	"Male":[gender],
# 	"Bachelor's":[b],
# 	"Master's":[m],
# 	"PhD":[p]})

# st.dataframe(df)
# result=round(model.predict(df)[0][0],2)
# st.write(result)
# st.write("success")
# print(result)
# st.balloons()
# # st.snow()
# education = st.selectbox("Education Level", ["Bachelor's", "Master's", "PhD"])

# # One-hot encoding
# b = 1 if education == "Bachelor's" else 0
# m = 1 if education == "Master's" else 0
# p = 1 if education == "PhD" else 0

# df = pd.DataFrame({
#     "Age": [age],
#     "Years of Experience": [exp],
#     "Male": [gender],
#     "Bachelor's": [b],
#     "Master's": [m],
#     "PhD": [p]
# })

# st.dataframe(df)

# result = round(model.predict(df)[0][0], 2)
# st.write(result)
# st.write("success")
# print(result)
# st.balloons()
# st.snow()
