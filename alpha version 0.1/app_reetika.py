# app.py
import streamlit as st
import pandas as pd
import io
import json 
from ydata_profiling import ProfileReport

def load_data(uploaded_file):
    """
    Load data from various file types with improved JSON handling
    """
    try:
        if uploaded_file.type == 'text/csv':
            return pd.read_csv(uploaded_file)
        elif uploaded_file.type == 'application/json':
            # Handle different JSON structures
            data = json.load(uploaded_file)
            
            # If JSON is a dictionary with a key containing a list
            if isinstance(data, dict):
                for key, value in data.items():
                    if isinstance(value, list):
                        return pd.DataFrame(value)
            
            # If JSON is directly a list
            if isinstance(data, list):
                return pd.DataFrame(data)
            
            # Fallback to direct conversion
            return pd.json_normalize(data)
        
        elif uploaded_file.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            return pd.read_excel(uploaded_file)
        elif uploaded_file.type == 'application/octet-stream':
            return pd.read_parquet(uploaded_file)
    
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None

def main():
    st.title('ETL Demo - File Viewer')
    
    # File upload
    uploaded_file = st.file_uploader(
        "Choose a file", 
        type=['csv', 'json', 'xlsx', 'parquet']
    )
    
    if uploaded_file is not None:
        # Load data
        df = load_data(uploaded_file)
        
        if df is not None:
            # Display first 10 rows
            st.subheader('First 10 Rows')
            st.dataframe(df.head(10))
            
            # Pandas Profiling
            st.subheader('Pandas Profiling Report')
            if st.button('Generate Profile Report'):
                profile = ProfileReport(df, title='Pandas Profiling Report')
                
                # Save profile report
                profile_html = profile.to_html()
                st.download_button(
                    label="Download Full Report",
                    data=profile_html,
                    file_name='profile_report.html',
                    mime='text/html'
                )
                
                # Embed report preview
                st.components.v1.html(profile_html, height=600, scrolling=True)

if __name__ == '__main__':
    main()
