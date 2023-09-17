import streamlit as st
import json
import pandas as pd
import matplotlib.pyplot as plt

st.title("ESG Risk Assessment Summary")

# Load data
esg_summary_file = "esg_summary.json"
esg_scores_file = "esg_scores.json"
plot_filename = "yearly_esg_risks_plot.png"

with open(esg_summary_file, 'r') as f:
    summaries_data = json.load(f)

with open(esg_scores_file, 'r') as f:
    esg_scores = json.load(f)

# Convert ESG scores to DataFrame
esg_scores_df = pd.DataFrame.from_dict(esg_scores, orient='index')

# Display general summary
st.header("General ESG Risks Summary")
st.write(
    """
    Based on the analysis of the company's annual reports, the evaluation of the company's ESG (Environmental, Social, Governance) risks is as follows:
    - **Environmental Risks**: Lack of specific goals to reduce greenhouse gas emissions, limited disclosure on minimizing water and energy consumption, limited information on waste management and recycling initiatives.
    - **Social Risks**: Lack of adequate disclosure on employee diversity and inclusion initiatives, limited information on health and safety policies and procedures.
    - **Governance Risks**: Potential concerns about tax avoidance or using regulatory loopholes due to the company's registration in Delaware.
    """
)

# Display yearly ESG risk scores plot
st.header("Yearly ESG Risk Scores")
st.image(plot_filename, caption="Year-over-Year ESG Risk Scores", use_column_width=True)

# Display detailed analysis and recommendations
st.header("Detailed Analysis and Recommendations")

st.subheader("1. Detailed Analysis by Category:")
st.write(
    """
    - **Environmental Risks**: The company lacks specific targets for reducing emissions, which is a significant risk given the increasing global focus on climate change.
    - **Social Risks**: The lack of disclosed initiatives indicates that the company may not be fully embracing the benefits of a diverse workforce.
    - **Governance Risks**: The consistent score in this category raises questions about the company's adherence to regulations and reporting standards.
    """
)

st.subheader("2. Recommendations for Engagement:")
st.write(
    """
    - **Set Emission Targets**: Encourage the company to establish and disclose specific targets for reducing greenhouse gas emissions.
    - **Diversity Initiatives**: Advocate for transparent reporting on diversity and inclusion initiatives.
    """
)

st.subheader("3. Risk Mitigation Strategies:")
st.write(
    """
    - **Due Diligence**: Continual monitoring of the company's ESG practices to assess improvements or deteriorations.
    - **ESG-linked Financial Instruments**: Consider investing through financial instruments that are linked to the company meeting certain ESG criteria.
    """
)

st.subheader("4. Peer Comparison:")
st.write(
    """
    To make a more informed investment decision, you could compare the company's ESG scores against industry averages or leaders.
    """
)

# Display individual yearly summaries as a dropdown selection
st.header("Individual Yearly Summaries")
year = st.selectbox("Select Year", list(reversed(sorted(summaries_data.keys()))))
st.write(summaries_data[year]["summary"])
pdf_path = f"data/{year}/{year} Annual Report.pdf"
with open(pdf_path, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
st.download_button("Download PDF", PDFbyte, "application/pdf")
