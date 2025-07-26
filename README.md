Live On : [smartdatavis.streamlit.app](https://smartdatavis.streamlit.app/)

<img width="1919" height="966" alt="Screenshot 2025-07-26 181731" src="https://github.com/user-attachments/assets/4d537e51-3694-4cb2-8261-4e9b23a94f5f" />

# 📊 Smart Data Visualizer

An interactive and user-friendly data visualization web application built with **Streamlit**. This tool empowers users to perform quick Exploratory Data Analysis (EDA) by simply uploading a dataset and selecting the visualization types, without writing a single line of code.
an interactive web-based data visualization tool using Streamlit, allowing users to upload CSV, Excel, or JSON datasets and explore them with dynamic charts including histograms, line plots, scatter plots, bar charts, and heatmaps. Integrated Plotly and Seaborn for rich visualizations and employed pandas for efficient data handling. Designed an intuitive sidebar interface for selecting chart types and columns, supporting both numerical and categorical insights. Ensured support for real-time rendering of plots directly in the browser with zero code from the user's side.

## 🔧 Features

- 📂 Upload support for `.csv`, `.xlsx`, and `.json` datasets
- 🧮 Auto-detection of numerical and categorical columns
- 📊 Dynamic visualizations using **Plotly** and **Seaborn**
    - Histogram
    - Line Chart
    - Bar Chart
    - Scatter Plot
    - Heatmap
    - Statistical Summary
- 🧠 Responsive sidebar UI to configure plot settings
- 📈 Preview top rows of the dataset for quick inspection
- 💡 Error handling for unsupported files and missing data

## 🛠️ Tech Stack

- **Frontend/UI**: [Streamlit](https://streamlit.io/)
- **Visualization Libraries**: [Plotly](https://plotly.com/python/), [Seaborn](https://seaborn.pydata.org/)
- **Data Handling**: [pandas](https://pandas.pydata.org/)
- **Backend**: Python 3.x

## 🚀 Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/smart-data-visualizer.git
   cd smart-data-visualizer

