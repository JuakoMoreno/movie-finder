from backend_funcs import *

st.set_page_config(
    page_title="Movie Finder App",
    page_icon="📁",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.header("Used Dataset")
st.subheader('"Movies on Netflix, Prime Video, Hulu and Disney+"')
st.divider()
st.dataframe(df)
st.caption("Source: "+"https://www.kaggle.com/datasets/ruchi798/movies-on-netflix-prime-video-hulu-and-disney")
st.divider()