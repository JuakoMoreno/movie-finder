#streamlit run main.py
from backend_funcs import *

st.set_page_config(
    page_title="Movie Finder App",
    page_icon="🎥",
    layout="centered",
    initial_sidebar_state="expanded",
)
st.title("Movie Finder")

movieName = st.text_input("What movie do you want to watch?")
if (movieName):
    movieNameSearch = r'\b{}\b'.format(movieName)
    colName,colResults = st.columns(2)
    colName.write("Your results for: "+movieName)
    query_df = df[df['Title'].str.contains(movieNameSearch,case=False)]
    colResults.write("Total Results: "+ str(len(query_df)))
    ##st.dataframe(query_df)
    query_select = query_df.Title
    selected_movie = st.selectbox("Possible results:", query_select)
    if (selected_movie):
        st.text("Movie Searched: "+ selected_movie)
        rotten_value = query_df[query_df['Title'] == selected_movie]['Rotten Tomatoes'].iloc[0]
        ##rotten_value
        rotten_rating = rotten_value.split('/')[0]
        st.metric("Rotten Tomatoes",rotten_rating+" %")
        ################################
        isinNetflix = query_df[query_df['Title'] == selected_movie]['Netflix'].iloc[0]
        isinHulu = query_df[query_df['Title'] == selected_movie]['Hulu'].iloc[0]
        isinPrime = query_df[query_df['Title'] == selected_movie]['Prime Video'].iloc[0]
        isinDisney = query_df[query_df['Title'] == selected_movie]['Disney+'].iloc[0]

        ##isinNetflix
        ##isinHulu
        ##isinPrime
        ##isinDisney
        ################################
        st.write("You can find that movie in: ")
        colNetflix,colHulu,colPrime,colDisney = st.columns(4)
        if(isinNetflix):
            colNetflix.image(imageNetflix)
            colNetflix.text("NETFLIX")
        if(isinHulu):
            colHulu.image(imageHulu)
            colHulu.text("HULU")
        if(isinPrime):
            colPrime.image(imagePrime)
            colPrime.text("PRIME VIDEO")
        if(isinDisney):
            colDisney.image(imageDisney)
            colDisney.text("DISNEY+")