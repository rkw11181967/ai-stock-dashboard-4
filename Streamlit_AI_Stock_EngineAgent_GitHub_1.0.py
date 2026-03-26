import streamlit as st
import requests
import pandas as pd

st.set_page_config(layout="wide")
st.title("📊 AI Stock Dashboard + Signal Engine")

# ------------------------
# LOAD ALERTS FROM GITHUB
# ------------------------
st.subheader("🚨 Top AI Trade Signals")

url = "https://raw.githubusercontent.com/rkw11181967/ai-stock-dashboard-4/main/alerts.json"

try:
    response = requests.get(url)
    alerts = response.json()

    if alerts:

        df = pd.DataFrame(alerts)

        st.dataframe(df)

        for a in alerts:

            text = f"""
Ticker: {a['ticker']}
Type: {a['type']}
Confidence: {a['confidence']}
Score: {a['directional_score']}
Technical: {a['signal']}
Headlines: {a['headlines']}
"""

            if "BUY" in a["type"]:
                st.success(text)

            elif "SELL" in a["type"]:
                st.error(text)

            else:
                st.warning(text)

    else:
        st.info("No signals yet")

except:
    st.warning("⚠️ Could not load alerts.json")

# ------------------------
# REFRESH BUTTON
# ------------------------
if st.button("🔄 Refresh Alerts"):
    st.rerun()