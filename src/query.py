import streamlit as st 
from base import Base

base_csv_file = r'C:\Users\patty\OneDrive\Desktop\Streamlit\Streamlit-Assignment\netflix_list.csv'

netflix_names = st.text_input('Enter the name of the show/movie:' , value='').lower()

if netflix_names:
    base = Base()
    netflix_data = base.get_netflix_data(netflix_names)

    if netflix_data:
        st.write(netflix_data)
        type = netflix_data.get('type', 0)
        if isinstance(type, str):
            if type == 'movie':
                st.image('https://images.creativemarket.com/0.1.0/ps/7414066/600/400/m2/fpnw/wm1/logo-design-for-movie-production-company-01-.jpg?1575502358&s=50e3d37c1ab493df98baf6eb75f2a430&fmt=webp', caption='Movie')
            elif type == 'tvSeries':
                st.image('https://img.freepik.com/premium-vector/tv-show-neon-sign-style-text_44523-738.jpg?w=1380',caption='tvshow')
            else:
                st.write('Show/Movie not available')
        else:
            st.write('Show/Movie no info available')
    else:
        st.write('Show/Movie not available')
