import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


def load_data(uploaded_file):
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file)
        elif uploaded_file.name.endswith('.json'):
            df = pd.read_json(uploaded_file)
        else:
            st.error("Unsupported file format. Please upload CSV, Excel, or JSON.")
            return None
        return df
    except Exception as e:
        st.error(f"⚠ Error loading file: {e}")
        return None

# Streamlit UI
st.set_page_config(page_title="📊 Smart Data Visualizer", layout="wide")
st.title("📊 Smart Data Visualizer")

# Sidebar Settings
st.sidebar.title("⚙️ Settings")
uploaded_file = st.file_uploader("📂 Upload your dataset (CSV, Excel, or JSON)", type=['csv', 'xlsx', 'json'])

if uploaded_file:
    df = load_data(uploaded_file)
    if df is not None:
        st.subheader("Data Preview")
        st.dataframe(df.head())

        # Identify column types
        numeric_cols = df.select_dtypes(include=['number']).columns
        categorical_cols = df.select_dtypes(include=['object', 'category']).columns

        st.sidebar.subheader("📊 Choose Visualization")
        chart_type = st.sidebar.selectbox(
            "Chart Type", 
            ["Histogram", "Line Chart", "Bar Chart", "Scatter Plot", "Box Plot", "Heatmap", "Statistical Summary"]
        )
        st.subheader(f"📈 {chart_type}")

        if chart_type == "Histogram":
            col = st.sidebar.selectbox("Select Numeric Column", numeric_cols)
            if col:
                fig = px.histogram(df, x=col, title=f"Histogram of {col}")
                st.plotly_chart(fig)

        elif chart_type == "Line Chart":
            x = st.sidebar.selectbox("X-axis", df.columns)
            y = st.sidebar.selectbox("Y-axis", numeric_cols)
            if x and y:
                fig = px.line(df, x=x, y=y, title=f"Line Chart ({x} vs {y})")
                st.plotly_chart(fig)

        elif chart_type == "Bar Chart":
            x = st.sidebar.selectbox("X-axis (Categorical)", categorical_cols)
            y = st.sidebar.selectbox("Y-axis (Numeric)", numeric_cols)
            if x and y:
                fig = px.bar(df, x=x, y=y, title=f"Bar Chart ({x} vs {y})")
                st.plotly_chart(fig)

        elif chart_type == "Scatter Plot":
            x = st.sidebar.selectbox("X-axis (Numeric)", numeric_cols)
            y = st.sidebar.selectbox("Y-axis (Numeric)", numeric_cols)
            if x and y:
                fig = px.scatter(df, x=x, y=y, title=f"Scatter Plot ({x} vs {y})")
                st.plotly_chart(fig)

        elif chart_type == "Box Plot":
            num = st.sidebar.selectbox("Numeric Column", numeric_cols)
            cat = st.sidebar.selectbox("Group by (Categorical)", [None] + list(categorical_cols))
            if num:
                if cat:
                    fig = px.box(df, x=cat, y=num, title=f"Box Plot of {num} by {cat}")
                else:
                    fig = px.box(df, y=num, title=f"Box Plot of {num}")
                st.plotly_chart(fig)

        elif chart_type == "Heatmap":
            corr_df = df.select_dtypes(include=['number']).corr()
            if corr_df.empty:
                st.error("No numeric columns for correlation heatmap.")
            else:
                fig, ax = plt.subplots(figsize=(10, 6))
                sns.heatmap(corr_df, annot=True, cmap="viridis", ax=ax)
                st.pyplot(fig)

        elif chart_type == "Statistical Summary":
            st.markdown("### Descriptive Statistics")
            st.write(df.describe().T)
            st.markdown("### Data Overview")
            overview = pd.DataFrame({
                'Data Type': df.dtypes,
                'Non-Null Count': df.count(),
                'Null Count': df.isnull().sum(),
                'Unique Values': df.nunique()
            })
            st.write(overview)

# Footer
st.sidebar.markdown("---")
st.sidebar.info("Created by Vaibhav.")

