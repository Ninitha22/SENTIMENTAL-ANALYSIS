import streamlit as st 
import requests 
# PAGE CONFIG 
st.set_page_config(
    page_title="SENTIMENT ANALYSIS" ,
    page_icon = "🎬",
    layout = "centered"
)
st.title("🎬 PRODUCT REVIEW SENTIMENT ANALYZER")
st.write("Enter a product review and get instant sentiment prediction ! ")
# input box 
review = st.text_area("Enter your product review here : " , height = 150)
# Predict button  
if st.button("Analyze Sentiment") :
    if review.strip() == "" :
        st.warning("Please enter a review first! ")
    else :
        with st.spinner("Analyzing........"):
            # call your flask backend 
           response = requests.post(
    "https://sentimental-analysis-lk81.onrender.com/predict",
    json={"reviews": review},
    timeout=60
)

st.write("STATUS CODE:", response.status_code)

st.write("SERVER RESPONSE:", response.text)

st.write("CONTENT TYPE:", response.headers.get("Content-Type"))
            )
            result = response.json()
        # display result 
        sentiment = result["prediction"]
        #confidence = result["confidence"]
        if "positive" in sentiment or "negative" in sentiment :
            st.success(f"Sentiment : {sentiment}")
        else : 
            st.error(f"Sentiment : {sentiment}")
        # st.metric(label = "Confidence" , value = confidence)
        
