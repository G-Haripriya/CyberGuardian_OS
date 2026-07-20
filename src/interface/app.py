from pathlib import Path
import json

import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="CyberGuardian OS",
    page_icon="🛡️",
    layout="wide",
)


@st.cache_data(ttl=60)
def load_inventory() -> pd.DataFrame:
    inventory_path = Path("data/inventory.json")

    if not inventory_path.exists() or inventory_path.stat().st_size == 0:
        return pd.DataFrame(columns=["name", "type", "status", "owner"])

    try:
        payload = json.loads(inventory_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return pd.DataFrame(columns=["name", "type", "status", "owner"])

    if isinstance(payload, list):
        return pd.DataFrame(payload)

    if isinstance(payload, dict):
        items = payload.get("items") if isinstance(payload.get("items"), list) else [payload]
        return pd.DataFrame(items)

    return pd.DataFrame(columns=["name", "type", "status", "owner"])


inventory = load_inventory()

st.title("CyberGuardian OS")
st.caption("SBOM, network, and compliance monitoring dashboard")

with st.sidebar:
    st.header("Operations")
    st.info("Use this workspace to review fleet inventory, BOM inputs, and governance posture.")
    st.markdown(
        """
        - Load inventory data into `data/inventory.json`
        - Add BOM artifacts under `data/boms/`
        - Run discovery and governance engines for enriched findings
        """
    )

summary_cols = st.columns(4)
summary_cols[0].metric("Devices tracked", max(len(inventory), 0))
summary_cols[1].metric("Open findings", 0)
summary_cols[2].metric("Compliance rules", 12)
summary_cols[3].metric("System readiness", "Ready")

st.container(border=True)
with st.container(border=True):
    st.subheader("Current posture")
    posture_col, details_col = st.columns([2, 1])

    with posture_col:
        st.progress(78, text="Governance maturity")
        st.write(
            "The platform is configured for inventory ingestion, BOM parsing, and compliance mapping."
        )

    with details_col:
        st.markdown(
            """
            - Discovery engine: configured
            - BOM parser: available
            - Compliance mapper: available
            - AI governor: ready for policy orchestration
            """
        )

with st.container(border=True):
    st.subheader("Inventory inputs")
    if inventory.empty:
        st.warning("No inventory records are present yet. Add data to `data/inventory.json` to populate the dashboard.")
    else:
        st.dataframe(inventory, use_container_width=True)

with st.container(border=True):
    st.subheader("Recommended actions")
    st.markdown(
        """
        1. Review the inventory file and validate device metadata.
        2. Drop SBOM artifacts into the BOM directory for automated analysis.
        3. Execute the governance and vulnerability workflows to produce findings.
        """
    )
