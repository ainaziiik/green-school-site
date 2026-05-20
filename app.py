import streamlit as st

st.set_page_config(
    page_title="Green Future School",
    layout="wide"
)

# ---------- CSS ----------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #eef5eb, #dcebdd);
    font-family: 'Segoe UI', sans-serif;
}

.block-container {
    padding-top: 2rem;
}

/* NAVBAR */
.navbar {
    background: rgba(255,255,255,0.18);
    backdrop-filter: blur(14px);

    border-radius: 20px;
    padding: 18px 30px;

    display: flex;
    justify-content: space-between;
    align-items: center;

    margin-bottom: 25px;

    border: 1px solid rgba(255,255,255,0.25);

    box-shadow: 0 8px 32px rgba(0,0,0,0.05);
}

.logo {
    font-size: 26px;
    font-weight: 700;
    color: #2F3E34;
}

.menu {
    display: flex;
    gap: 30px;
}

.menu-item {
    color: #4F5E53;
    font-size: 16px;
    text-decoration: none;
    transition: 0.3s;
}

.menu-item:hover {
    color: #7FA98F;
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

/* SUBTITLE */
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

# ---------- NAVBAR ----------
st.markdown("""
<div class="navbar">

    <div class="logo">
        Green Future
    </div>

    <div class="menu">
        <a class="menu-item">Home</a>
        <a class="menu-item">About</a>
        <a class="menu-item">Teachers</a>
        <a class="menu-item">Gallery</a>
        <a class="menu-item">Contacts</a>
    </div>

</div>
""", unsafe_allow_html=True)


# ---------- HERO ----------
left, right = st.columns([1.2, 1])

with left:
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

with right:
    st.image(
        "https://images.unsplash.com/photo-1523050854058-8df90110c9f1",
        use_container_width=True
    )

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
