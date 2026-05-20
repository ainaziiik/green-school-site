import streamlit as st

st.set_page_config(
    page_title="Green Future School",
    layout="wide"
)

# ================= CSS =================
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #eef5eb, #dcebdd);
    font-family: 'Segoe UI', sans-serif;
}

.block-container {
    padding-top: 2rem;
    max-width: 1200px;
}

/* BACKGROUND BLUR */
.blur1 {
    position: fixed;
    width: 300px;
    height: 300px;
    background: rgba(127,169,143,0.35);
    border-radius: 50%;
    filter: blur(120px);

    top: -100px;
    left: -100px;

    z-index: -1;
}

.blur2 {
    position: fixed;
    width: 350px;
    height: 350px;
    background: rgba(190,220,200,0.4);
    border-radius: 50%;
    filter: blur(120px);

    bottom: -120px;
    right: -100px;

    z-index: -1;
}

/* NAVBAR */
.navbar {
    background: rgba(255,255,255,0.2);
    backdrop-filter: blur(14px);

    border-radius: 20px;
    padding: 18px 30px;

    display: flex;
    justify-content: space-between;
    align-items: center;

    margin-bottom: 30px;

    border: 1px solid rgba(255,255,255,0.25);

    box-shadow: 0 8px 32px rgba(0,0,0,0.05);
}

.logo {
    font-size: 28px;
    font-weight: 700;
    color: #2F3E34;
}

/* HERO */
.hero {
    background: rgba(255,255,255,0.22);
    backdrop-filter: blur(15px);

    padding: 60px;

    border-radius: 30px;

    border: 1px solid rgba(255,255,255,0.3);

    box-shadow: 0 8px 32px rgba(0,0,0,0.08);
}

.title {
    font-size: 58px;
    font-weight: 700;
    color: #2F3E34;
}

.subtitle {
    font-size: 20px;
    color: #5E6E63;
    margin-top: 15px;
    line-height: 1.6;
}

/* IMAGE */
.hero-img img {
    border-radius: 30px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.08);
}

/* CARDS */
.card {
    background: rgba(255,255,255,0.22);

    backdrop-filter: blur(14px);

    border-radius: 25px;

    padding: 30px;

    margin-top: 25px;

    border: 1px solid rgba(255,255,255,0.25);

    box-shadow:
        8px 8px 20px rgba(0,0,0,0.06),
        -8px -8px 20px rgba(255,255,255,0.4);

    transition: 0.3s;
}

.card:hover {
    transform: translateY(-5px);
}

.card-title {
    font-size: 28px;
    font-weight: 600;
    color: #2F3E34;
}

.card-text {
    font-size: 16px;
    color: #5E6E63;
    margin-top: 10px;
    line-height: 1.6;
}

</style>
""", unsafe_allow_html=True)

# ================= BLURS =================
st.markdown("""
<div class="blur1"></div>
<div class="blur2"></div>
""", unsafe_allow_html=True)

# ================= NAVBAR =================
st.markdown("""
<div class="navbar">
    <div class="logo">
        Green Future
    </div>
</div>
""", unsafe_allow_html=True)

# ================= HERO =================
left, right = st.columns([1.2, 1])

with left:
    st.markdown('<div class="hero">', unsafe_allow_html=True)

    st.title("Green Future School")

    st.write(
        "Modern education for a new generation "
        "with creativity, innovation and technology."
    )

    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.image(
        "https://images.unsplash.com/photo-1509062522246-3755977927d7",
        use_container_width=True
    )

# ================= CARDS =================
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Achievements")

    st.write(
        "Students participate in olympiads, competitions and creative projects."
    )

    st.markdown('</div>', unsafe_allow_html=True)


with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Achievements")

    st.write(
        "Students participate in olympiads, competitions and creative projects."
    )

    st.markdown('</div>', unsafe_allow_html=True)


with col3:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Achievements")

    st.write(
        "Students participate in olympiads, competitions and creative projects."
    )

    st.markdown('</div>', unsafe_allow_html=True)

# ================= ABOUT =================
st.markdown("""
<div class="card">

<div class="card-title">
About School
</div>

<div class="card-text">
Green Future School is a modern educational
environment focused on creativity, innovation
and student development.
</div>

</div>
""", unsafe_allow_html=True)
