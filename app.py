import streamlit as st

import logic

# Let's make some color helpers

LEVEL_COLORS = {
    "Low": ("#c3e6cb", "#155724"),      # stronger green
    "Typical": ("#f2f2f2", "#333333"),  # unchanged
    "High": ("#f5c6cb", "#721c24")      # stronger red
}



def render_level(level):
    bg, fg = LEVEL_COLORS.get(level, ("#f2f2f2", "#333333"))
    return f"""
    <span style="
        display:inline-block;
        padding:6px 10px;
        border-radius:999px;
        background:{bg};
        color:{fg};
        font-weight:600;
        font-size:0.9rem;
        border:1px solid rgba(0,0,0,0.08);
    ">{level}</span>
    """

# Now on to the actual UI:

st.title("Vancouver Business Registrations: Inferences for Market Interpretation")

st.image("https://images.pexels.com/photos/29072584/pexels-photo-29072584.jpeg",
            caption="Vancouver Skyline (Credit: Luke Lawreszuk)",
            use_container_width= True)



# Dropdown menu

business_type = st.selectbox("Business Type", sorted(logic.big_types))

local_area = st.selectbox(
    "Neighbourhood (LocalArea)",
    sorted(logic.df_filtered["LocalArea"].dropna().unique()))


# Below has features to classify colors for metrics, classes, and has a button to go to the methods behind calculation.

if st.button("Run"):

    result = logic.market_interpretation(business_type, local_area)
    st.subheader(result["interpretation_title"])
    st.write(result["interpretation_summary"])

    st.subheader("Scores")

    c1, c2, c3 = st.columns([2, 1, 2])
    with c1:
        st.metric("Concentration score", f"{result['concentration_score']:.2f}")
    with c2:
        st.markdown(render_level(result["concentration_level"]), unsafe_allow_html=True)
    with c3:
        st.markdown(
    """
    <a href="#concentration" style="
        display:inline-block;
        padding:6px 10px;
        border-radius:8px;
        background:#f2f2f2;
        color:#666;
        text-decoration:none;
        border:1px solid rgba(0,0,0,0.08);
        font-size:0.85rem;
    ">How was this calculated?</a>
    """,
    unsafe_allow_html=True)

    c4, c5, c6 = st.columns([2, 1, 2])
    with c4:
        st.metric("Closure risk score", f"{result['closure_risk_score']:.2f}")
    with c5:
        st.markdown(render_level(result["closure_risk_level"]), unsafe_allow_html=True)
    with c6:
            st.markdown(
    """
    <a href="#closure-risk" style="
        display:inline-block;
        padding:6px 10px;
        border-radius:8px;
        background:#f2f2f2;
        color:#666;
        text-decoration:none;
        border:1px solid rgba(0,0,0,0.08);
        font-size:0.85rem;
    ">How was this calculated?</a>
    """,
    unsafe_allow_html=True)

    c7, c8, c9 = st.columns([2, 1, 2])
    with c7:
        rec = result["recency_score"]
        st.metric("Recency Score", "N/A" if rec is None else f"{rec:.2f}")
    with c8:
        st.markdown(render_level("Typical"), unsafe_allow_html=True)  # always neutral
    with c9:
             st.markdown(
    """
    <a href="#recency" style="
        display:inline-block;
        padding:6px 10px;
        border-radius:8px;
        background:#f2f2f2;
        color:#666;
        text-decoration:none;
        border:1px solid rgba(0,0,0,0.08);
        font-size:0.85rem;
    ">How was this calculated?</a>
    """,
    unsafe_allow_html=True)


  

    fig = logic.plot_map(business_type, local_area)

    st.plotly_chart(fig, use_container_width = True)

    st.divider()
    st.header("About this Project")

    st.markdown("""
     The City of Vancouver has a rich and diverse business landscape, something that represents this is a dataset in their Open Data Portal. 
    Said dataset holds records of the recent business registries from 2024 onwards. It is rather large, with over 130,000 registrations.
    I took this size as an opportunity to make inferences on the market as a whole. These inferences are based on factors such as the 
    concentration, recency, and closures of the registrations of a certain business type and location. As with anything involving data, it
    was imperative to 
                """)




