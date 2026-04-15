import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Dashboard Meta Ads + Orgánico", layout="wide")

st.title("Dashboard Meta Ads + Crecimiento Orgánico")
st.caption("Demo interactiva para visualizar KPIs blended (paid + orgánico)")

st.sidebar.header("Datos")
uploaded_file = st.sidebar.file_uploader("Sube tu CSV", type=["csv"])

REQUIRED_COLUMNS = [
    "date",
    "channel_group",
    "spend",
    "sessions",
    "purchases",
    "revenue",
    "new_customers",
]

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("data/sample_marketing_daily.csv")

missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
if missing:
    st.error(f"Faltan columnas requeridas: {', '.join(missing)}")
    st.stop()

df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = df.dropna(subset=["date"])

start_date = df["date"].min().date()
end_date = df["date"].max().date()

selected_dates = st.sidebar.date_input(
    "Rango de fechas",
    value=(start_date, end_date),
    min_value=start_date,
    max_value=end_date,
)

if not isinstance(selected_dates, tuple) or len(selected_dates) != 2:
    st.warning("Selecciona un rango de fechas válido.")
    st.stop()

start, end = selected_dates
mask = (df["date"].dt.date >= start) & (df["date"].dt.date <= end)
filtered = df.loc[mask].copy()

channels = st.sidebar.multiselect(
    "Canales",
    options=sorted(filtered["channel_group"].dropna().unique().tolist()),
    default=sorted(filtered["channel_group"].dropna().unique().tolist()),
)

if channels:
    filtered = filtered[filtered["channel_group"].isin(channels)]

if filtered.empty:
    st.warning("No hay datos para los filtros seleccionados.")
    st.stop()

paid = filtered[filtered["channel_group"].str.contains("paid", case=False, na=False)]
organic = filtered[filtered["channel_group"].str.contains("organic", case=False, na=False)]

total_spend = float(filtered["spend"].sum())
total_revenue = float(filtered["revenue"].sum())
total_purchases = float(filtered["purchases"].sum())
total_new_customers = float(filtered["new_customers"].sum())

paid_revenue = float(paid["revenue"].sum())
organic_revenue = float(organic["revenue"].sum())

mer = (total_revenue / total_spend) if total_spend > 0 else 0.0
cac_blended = (total_spend / total_new_customers) if total_new_customers > 0 else 0.0
roas_meta = (paid_revenue / float(paid["spend"].sum())) if float(paid["spend"].sum()) > 0 else 0.0
cvr = (total_purchases / float(filtered["sessions"].sum())) if float(filtered["sessions"].sum()) > 0 else 0.0

col1, col2, col3, col4, col5, col6 = st.columns(6)
col1.metric("Revenue Total", f"${total_revenue:,.0f}")
col2.metric("Revenue Paid", f"${paid_revenue:,.0f}")
col3.metric("Revenue Orgánico", f"${organic_revenue:,.0f}")
col4.metric("MER", f"{mer:.2f}")
col5.metric("CAC Blended", f"${cac_blended:,.2f}")
col6.metric("ROAS Paid", f"{roas_meta:.2f}")

trend = (
    filtered.groupby(["date", "channel_group"], as_index=False)
    .agg(spend=("spend", "sum"), revenue=("revenue", "sum"), purchases=("purchases", "sum"))
)

left, right = st.columns(2)
with left:
    fig_revenue = px.line(trend, x="date", y="revenue", color="channel_group", title="Revenue por canal")
    st.plotly_chart(fig_revenue, use_container_width=True)

with right:
    fig_spend = px.line(trend, x="date", y="spend", color="channel_group", title="Spend por canal")
    st.plotly_chart(fig_spend, use_container_width=True)

st.subheader("Tabla de performance por canal")
channel_table = (
    filtered.groupby("channel_group", as_index=False)
    .agg(
        spend=("spend", "sum"),
        sessions=("sessions", "sum"),
        purchases=("purchases", "sum"),
        revenue=("revenue", "sum"),
        new_customers=("new_customers", "sum"),
    )
)
channel_table["cvr"] = channel_table["purchases"] / channel_table["sessions"].replace(0, pd.NA)
channel_table["cpp"] = channel_table["spend"] / channel_table["purchases"].replace(0, pd.NA)
channel_table["roas"] = channel_table["revenue"] / channel_table["spend"].replace(0, pd.NA)

st.dataframe(channel_table, use_container_width=True)

st.markdown("---")
st.subheader("Cómo hacer deploy")
st.markdown(
    """
1. Haz fork o sube este repo a GitHub (idealmente público).
2. Ve a [share.streamlit.io](https://share.streamlit.io) y conecta tu GitHub.
3. Selecciona el repo, branch y archivo principal `app.py`.
4. Haz click en **Deploy**.
5. Abre y comparte la URL final de la app con formato `https://tu-app.streamlit.app` (no compartas la URL de `share.streamlit.io`).

Si ves **HTTP ERROR 401**:
- Revisa que estés usando la URL `*.streamlit.app` de la app desplegada.
- Si el repo/app está privado, habilita acceso público o agrega usuarios autorizados en Streamlit Cloud.
- Revisa que no exista un proxy corporativo bloqueando la sesión.

También puedes correrlo local:
```bash
pip install -r requirements.txt
streamlit run app.py
```
"""
)

st.caption(f"CVR total del periodo: {cvr:.2%}")
