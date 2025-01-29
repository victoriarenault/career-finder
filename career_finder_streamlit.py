import streamlit as st
import pandas as pd
st.image("https://raw.githubusercontent.com/victoriarenault/career-finder/main/logo.png", width=200)
# Load career data from Excel file
file_path = "Draft Master - Career Pathways.xlsx"

# Try to load the file
try:
    career_data = pd.read_excel(file_path)

    # Standardizing column names
    career_data.columns = career_data.columns.str.strip()
    career_data.rename(columns={"Recomended enrichments": "Recommended enrichments"}, inplace=True)

    # Function to search careers by subject or career name
    def search_career_or_subject(query):
        query = query.lower()
        results = career_data[
            career_data["Career:"].str.lower().str.contains(query, na=False) |
            career_data["Suitable subjects"].str.lower().str.contains(query, na=False)
        ]
        return results[["Career:", "Suitable subjects", "Recommended enrichments"]]

    # Streamlit Web App Interface
    st.title("🎓 Career Finder Tool 🔍")
    st.write("Enter a subject or career to explore relevant career paths, subjects, and enrichment activities.")

    query = st.text_input("🔎 Search by Subject or Career:")

    if query:
        results = search_career_or_subject(query)
        if results.empty:
            st.warning("No results found. Try another keyword!")
        else:
            st.write("### Matching Careers and Subjects:")
            st.dataframe(results)

except FileNotFoundError:
    st.error("Error: The file 'Draft Master - Career Pathways.xlsx' was not found. Please make sure it's in the same folder as this script.")
