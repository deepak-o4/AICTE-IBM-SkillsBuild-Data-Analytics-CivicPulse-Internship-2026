from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "processed" / "bbmp_grievances_clean.csv"
SUMMARY_PATH = ROOT / "data" / "processed" / "civicpulse_summary.json"

st.set_page_config(page_title="CivicPulse Dashboard", layout="wide")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');
    :root { --primary:#4099ff; --primary-light:#73b4ff; --purple:#7759de; --success:#2ed8b6; --danger:#ff5370; --slate:#3b4650; --border:#e2e5e8; }
    .stApp { background: #f6f7fb; color: #263238; font-family: 'Poppins', sans-serif; }
    [data-testid="stSidebar"] { background: linear-gradient(180deg, #3b4650 0%, #263238 100%); border-right: 0; }
    [data-testid="stSidebar"] * { color: #e8eef4; }
    [data-testid="stSidebar"] .stMultiSelect [data-baseweb="select"] > div { background: rgba(255,255,255,.09); border: 1px solid rgba(255,255,255,.18); }
    [data-testid="stSidebar"] [data-baseweb="tag"] { background: linear-gradient(45deg, var(--primary), var(--primary-light)); border: 0; }
    div.block-container { padding: 2rem 2.5rem 3rem; max-width: 1500px; }
    .pc-brand { padding: .25rem 0 1.4rem; border-bottom: 1px solid rgba(255,255,255,.14); margin-bottom: 1.4rem; }
    .pc-brand-mark { display:inline-flex; width:38px; height:38px; align-items:center; justify-content:center; border-radius:12px; margin-right:9px; color:white; font-weight:700; font-size:19px; background:linear-gradient(45deg,var(--purple),var(--primary)); box-shadow:0 6px 16px rgba(64,153,255,.35); }
    .pc-brand-name { color:white; font-size:20px; font-weight:700; vertical-align:middle; }
    .pc-eyebrow { color:#748892; font-size:12px; letter-spacing:.08em; text-transform:uppercase; font-weight:600; }
    h1 { color:#263238; font-weight:700 !important; letter-spacing:-.02em; }
    h2, h3 { color:#263238; font-weight:600 !important; }
    .stCaption { color:#748892 !important; }
    [data-testid="stMetric"] { background:white; border:0; border-top:4px solid var(--primary); border-radius:5px; padding:1.25rem 1.35rem; box-shadow:0 1px 2.94px .06px rgba(4,26,55,.16); transition:all .2s ease-in-out; }
    [data-testid="stMetric"]:hover { box-shadow:0 0 25px -5px #9e9c9e; transform:translateY(-2px); }
    [data-testid="stMetricLabel"] { color:#748892 !important; font-size:13px !important; }
    [data-testid="stMetricValue"] { color:#263238 !important; font-weight:600; }
    div[data-testid="stHorizontalBlock"] > div:nth-child(2) [data-testid="stMetric"] { border-top-color:var(--success); }
    div[data-testid="stHorizontalBlock"] > div:nth-child(3) [data-testid="stMetric"] { border-top-color:var(--purple); }
    div[data-testid="stHorizontalBlock"] > div:nth-child(4) [data-testid="stMetric"] { border-top-color:var(--danger); }
    .stPlotlyChart { background:white; border-radius:5px; box-shadow:0 1px 2.94px .06px rgba(4,26,55,.16); padding:.35rem; }
    [data-testid="stDataFrame"] { border:1px solid var(--border); border-radius:5px; }
    </style>
    """,
    unsafe_allow_html=True,
)

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)
    df["Grievance Date"] = pd.to_datetime(df["Grievance Date"], errors="coerce")
    df["Year"] = df["Grievance Date"].dt.year
    return df

@st.cache_data
def load_summary():
    return pd.read_json(SUMMARY_PATH)


df = load_data()
summary = load_summary()

st.sidebar.markdown(
    '<div class="pc-brand"><span class="pc-brand-mark">C</span><span class="pc-brand-name">CivicPulse</span></div>',
    unsafe_allow_html=True,
)
st.sidebar.markdown('<div class="pc-eyebrow">Analytics navigation</div>', unsafe_allow_html=True)
st.sidebar.markdown("### Dashboard filters")

st.title("CivicPulse — BBMP Grievance Intelligence")
st.caption("Ward-wise Civic Demand, Grievance Trends & Municipal Decision Analytics")

years = sorted(df["Year"].unique())
selected_years = st.sidebar.multiselect("Select years", years, default=years)
selected_categories = st.sidebar.multiselect(
    "Select categories",
    sorted(df["Category"].unique()),
    default=sorted(df["Category"].unique()),
)
selected_statuses = st.sidebar.multiselect(
    "Select grievance status",
    sorted(df["Grievance Status"].unique()),
    default=sorted(df["Grievance Status"].unique()),
)

filtered = df[
    df["Year"].isin(selected_years)
    & df["Category"].isin(selected_categories)
    & df["Grievance Status"].isin(selected_statuses)
].copy()

if filtered.empty:
    st.warning("No rows match the selected filters.")
    st.stop()

kpis = {
    "Total grievances": int(len(filtered)),
    "Unique wards": int(filtered["Ward Name"].nunique()),
    "Unique categories": int(filtered["Category"].nunique()),
    "Top category": filtered["Category"].value_counts().index[0],
    "Top ward": filtered["Ward Name"].value_counts().index[0],
}

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total grievances", f"{kpis['Total grievances']:,}")
col2.metric("Unique wards", f"{kpis['Unique wards']}")
col3.metric("Unique categories", f"{kpis['Unique categories']}")
col4.metric("Top category", kpis["Top category"])

st.markdown('<div class="pc-eyebrow">Demand overview</div>', unsafe_allow_html=True)
trend = filtered.groupby("Year").size().reset_index(name="complaints")
trend["Year"] = trend["Year"].astype(str)
fig_trend = px.line(
    trend,
    x="Year",
    y="complaints",
    markers=True,
    title="Yearly complaint trend",
    category_orders={"Year": [str(year) for year in years]},
)
fig_trend.update_layout(
    template="plotly_white",
    height=360,
    xaxis_title="Year",
    yaxis_title="Complaints",
    font={"family": "Poppins, sans-serif", "color": "#748892"},
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    margin={"l": 55, "r": 25, "t": 55, "b": 45},
)
fig_trend.update_traces(line={"color": "#4099ff", "width": 3}, marker={"color": "#7759de", "size": 9})

cat = filtered["Category"].value_counts().head(8).reset_index()
cat.columns = ["Category", "Complaints"]
fig_cat = px.bar(cat, x="Complaints", y="Category", orientation="h", title="Top complaint categories")
fig_cat.update_layout(template="plotly_white", height=360, font={"family": "Poppins, sans-serif", "color": "#748892"}, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", margin={"l": 10, "r": 20, "t": 55, "b": 35})
fig_cat.update_traces(marker_color="#4099ff")

ward = filtered["Ward Name"].value_counts().head(8).reset_index()
ward.columns = ["Ward", "Complaints"]
fig_ward = px.bar(ward, x="Complaints", y="Ward", orientation="h", title="Highest-demand wards")
fig_ward.update_layout(template="plotly_white", height=360, font={"family": "Poppins, sans-serif", "color": "#748892"}, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", margin={"l": 10, "r": 20, "t": 55, "b": 35})
fig_ward.update_traces(marker_color="#2ed8b6")

status = filtered["Grievance Status"].value_counts().reset_index()
status.columns = ["Status", "Complaints"]
fig_status = px.pie(status, names="Status", values="Complaints", title="Status distribution")
fig_status.update_layout(template="plotly_white", height=360, font={"family": "Poppins, sans-serif", "color": "#748892"}, paper_bgcolor="rgba(0,0,0,0)", margin={"l": 10, "r": 10, "t": 55, "b": 20}, legend={"orientation": "h", "y": -0.1})
fig_status.update_traces(marker={"colors": ["#4099ff", "#7759de", "#2ed8b6", "#ffb64d", "#ff5370", "#00bcd4", "#748892", "#263238"]})

st.plotly_chart(fig_trend, use_container_width=True)
left, right = st.columns(2)
left.plotly_chart(fig_cat, use_container_width=True)
right.plotly_chart(fig_ward, use_container_width=True)

st.plotly_chart(fig_status, use_container_width=True)

st.subheader("Filtered dataset preview")
st.dataframe(filtered.head(50), use_container_width=True)
