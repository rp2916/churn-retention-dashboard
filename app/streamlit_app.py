import streamlit as st
import pandas as pd
from pathlib import Path

ROOT = Path("/Users/rhishabhpatil/Desktop/Portfolio/Churn_Dashboard")
OUT = ROOT / "outputs"

st.title("Customer Churn Dashboard")

# Load KPIs
kpi_df = pd.read_csv(OUT / "data" / "kpis.csv", index_col=0)

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Customers", int(kpi_df.loc["Total Customers","Value"]))
c2.metric("Churned Customers", int(kpi_df.loc["Churned Customers","Value"]))
c3.metric("Churn Rate (%)", kpi_df.loc["Churn Rate","Value"])
c4.metric("Revenue at Risk ($)", kpi_df.loc["Revenue at Risk ($)","Value"])

st.markdown("---")

st.components.v1.html((OUT / "figures" / "churn_kpis.html").read_text(), height=400)
st.components.v1.html((OUT / "figures" / "churn_risk.html").read_text(), height=400)