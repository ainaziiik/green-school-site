import streamlit as st

st.set_page_config(
    page_title="Green School",
    layout="wide",
)

# ---------- CSS ----------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #eef5eb, #dcebdd);
    font-family: 'Segoe UI', sans-serif;
}

/* HERO */
.hero {
    background: rgba(255,255,255,0.25);
    backdrop-filter: blur(15px);
    padding: 60px;
    border-radius: 30px;
    border: 1px solid rgba(255,255,255,0.3);
    box-shadow: 0 8px 32px rgba(0,0,0,0.08);
    margin-top: 20px;
}

/* TITLE */
.title {
    font-size: 56px;
    font-weight: 700;
    color: #2F3E34;
}

.subtitle {
    font-size: 20px;
    color: #5E6E63;
    margin-top: 10px;
}

/* CARDS */
.card {
    background: rgba(255,255,255,0.22);
    backdrop-filter: blur(14px);
    border-radius: 25px;
    padding: 30px;
    margin-top: 20px;
    border: 1px solid rgba(255,255,255,0.25);

    box-shadow:
        8px 8px 20px rgba(0,0,0,0.06),
        -8px -8px 20px rgba(255,255,255,0.4);

    transition: 0.3s;
}

.card:hover {
    transform: translateY(-5px);
}

/* CARD TITLE */
.card-title {
    font-size: 28px;
    font-weight: 600;
    color: #2F3E34;
}

/* CARD TEXT */
.card-text {
    font-size: 16px;
    color: #5E6E63;
    margin-top: 10px;
}

</style>
""", unsafe_allow_html=True)

# ---------- HERO ----------
st.markdown("""
<div class="hero">
    <div class="title">
        Green Future School
    </div>

    <div class="subtitle">
        Modern education for a new generation
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- CARDS ----------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-title">Achievements</div>
        <div class="card-text">
            Students participate in olympiads, competitions and creative projects.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-title">School Life</div>
        <div class="card-text">
            Events, sports, clubs and unforgettable memories every year.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <div class="card-title">Teachers</div>
        <div class="card-text">
            Experienced teachers supporting every student’s growth.
        </div>
    </div>
    """, unsafe_allow_html=True)
