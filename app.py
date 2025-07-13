import streamlit as st

st.set_page_config(page_title="Laptop Price Predictor", layout="centered")

# st.image("laptop_image.jpg", use_column_width=True)

st.markdown("## 💻 Laptop Price Prediction App")
st.write("Use machine learning to predict laptop prices and explore feature-based data insights.")

col1, col2 = st.columns(2)

with col1:
    if st.button("🔮 Predict Laptop Price"):
        st.switch_page("pages/Prediction.py")  

with col2:
    if st.button("📊 View Data Analysis"):
        st.switch_page("pages/Analysis.py")
