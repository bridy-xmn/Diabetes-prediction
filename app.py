import streamlit as st
import joblib
import pandas as pd

# 모델 불러오기
model = joblib.load("model.pkl")

st.title("🩺 Diabetes Risk Prediction")

st.write("Please enter your health information.")
st.markdown("""
Please complete the following health questionnaire.
The AI model will estimate your risk of diabetes based on your responses.
""")

HighBP = st.radio("High Blood Pressure", ["No", "Yes"])
HighBP = 1 if HighBP == "Yes" else 0

HighChol = st.radio("High Cholesterol", ["No", "Yes"])
HighChol = 1 if HighChol == "Yes" else 0

CholCheck = st.radio("Cholesterol Check in Last 5 Years", ["No", "Yes"])
CholCheck = 1 if CholCheck == "Yes" else 0

BMI = st.slider("BMI", 10, 60, 25)

Smoker = st.radio("Smoker", ["No", "Yes"])
Smoker = 1 if Smoker == "Yes" else 0

Stroke = st.radio("History of Stroke", ["No", "Yes"])
Stroke = 1 if Stroke == "Yes" else 0

HeartDiseaseorAttack = st.radio("Heart Disease or Heart Attack", ["No", "Yes"])
HeartDiseaseorAttack = 1 if HeartDiseaseorAttack == "Yes" else 0

PhysActivity = st.radio("Physical Activity", ["No", "Yes"])
PhysActivity = 1 if PhysActivity == "Yes" else 0

Fruits = st.radio("Eat Fruits Regularly", ["No", "Yes"])
Fruits = 1 if Fruits == "Yes" else 0

Veggies = st.radio("Eat Vegetables Regularly", ["No", "Yes"])
Veggies = 1 if Veggies == "Yes" else 0

HvyAlcoholConsump = st.radio("Heavy Alcohol Consumption", ["No", "Yes"])
HvyAlcoholConsump = 1 if HvyAlcoholConsump == "Yes" else 0

AnyHealthcare = st.radio("Have Health Care Coverage", ["No", "Yes"])
AnyHealthcare = 1 if AnyHealthcare == "Yes" else 0

NoDocbcCost = st.radio("Couldn't See Doctor Due to Cost", ["No", "Yes"])
NoDocbcCost = 1 if NoDocbcCost == "Yes" else 0

GenHlth = st.slider("General Health (1~5)", 1, 5, 3)
MentHlth = st.slider("Poor Mental Health Days", 0, 30, 0)
PhysHlth = st.slider("Poor Physical Health Days", 0, 30, 0)

DiffWalk = st.radio("Difficulty Walking", ["No", "Yes"])
DiffWalk = 1 if DiffWalk == "Yes" else 0

Sex = st.radio("Sex", ["Female", "Male"])
Sex = 1 if Sex == "Male" else 0
age_options = [
    "18-24","25-29","30-34","35-39","40-44","45-49",
    "50-54","55-59","60-64","65-69","70-74","75-79","80+"
]

Age = st.selectbox("Age Group", age_options)
Age = age_options.index(Age) + 1
education_options = [
    "Never attended school or kindergarten",
    "Elementary school",
    "Some high school",
    "High school graduate",
    "Some college or technical school",
    "College graduate"
]

Education = st.selectbox("Education Level", education_options)
Education = education_options.index(Education) + 1
income_options = [
    "< $10,000",
    "$10,000 - $14,999",
    "$15,000 - $19,999",
    "$20,000 - $24,999",
    "$25,000 - $34,999",
    "$35,000 - $49,999",
    "$50,000 - $74,999",
    "$75,000 or more"
]

Income = st.selectbox("Annual Household Income", income_options)
Income = income_options.index(Income) + 1

if st.button("Predict"):
    data = pd.DataFrame([[

        HighBP,
        HighChol,
        CholCheck,
        BMI,
        Smoker,
        Stroke,
        HeartDiseaseorAttack,
        PhysActivity,
        Fruits,
        Veggies,
        HvyAlcoholConsump,
        AnyHealthcare,
        NoDocbcCost,
        GenHlth,
        MentHlth,
        PhysHlth,
        DiffWalk,
        Sex,
        Age,
        Education,
        Income

    ]], columns=[
        'HighBP','HighChol','CholCheck','BMI','Smoker',
        'Stroke','HeartDiseaseorAttack','PhysActivity',
        'Fruits','Veggies','HvyAlcoholConsump',
        'AnyHealthcare','NoDocbcCost','GenHlth',
        'MentHlth','PhysHlth','DiffWalk',
        'Sex','Age','Education','Income'
    ])

    probability = model.predict_proba(data)[0][1]

    st.subheader(f"Diabetes Risk : {probability*100:.1f}%")
    st.progress(float(probability))

    st.metric(
        label="Diabetes Risk",
        value=f"{probability * 100:.1f}%"
    )

    if probability >= 0.3:
        st.error("⚠️ High Risk")
    else:
        st.success("✅ Low Risk")