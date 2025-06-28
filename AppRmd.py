import streamlit as st
import pickle
import pandas as pd 

st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f2f6; /* Light gray background */
    }
    </style>
    """,
    unsafe_allow_html=True
)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
    
    
        
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies  # ✅ fixed

# Load pickled data
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

# Streamlit app
st.title('𝔖𝔪𝔞𝔯𝔱 𝔐𝔬𝔳𝔦𝔢 ℜ𝔢𝔠𝔬𝔪𝔪𝔢𝔫𝔡𝔞𝔱𝔦𝔬𝔫 𝔖𝔶𝔰𝔱𝔢𝔪')

selected_movie_name = st.selectbox(
    'Select a movie',
    movies['title'].values)

if st.button('Recommend'):
    recommendation = recommend(selected_movie_name)
    st.write("Top 5 Recommendations:")
    for i in recommendation:
        st.write(i)
