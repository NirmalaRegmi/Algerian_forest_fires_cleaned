import streamlit as st
import pandas as pd

# Title of the app
st.title("Algerian Forest Fires Analysis")

# Description of the project
st.write("This project analyzes the Algerian forest fire dataset to predict the Fire Weather Index (FWI).")

# Upload dataset (use an appropriate path or let users upload a CSV)
uploaded_file = st.file_uploader(r"../Dataset/Algerian_forest_fires_cleaned.CSV", type=["csv"])

# Display the dataset
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Dataset Preview:")
    st.write(data)

    # Perform a simple analysis, like displaying summary statistics
    st.write("Summary Statistics:")
    st.write(data.describe())

    # Add your own custom analysis or visualizations here
    # Example: Plot histogram of temperature
    st.write("Temperature Distribution")
    st.bar_chart(data['Temperature'])  # Assuming 'Temperature' column exists

else:
    st.write("Please upload a CSV file to proceed.")

