import streamlit as st
st.title("Movie Ticket Management Dashboard")
above = {
    "Avengers: Endgame" : "18+",
    "The Dark Knight"   : "18+",
    "Inception"         : "18+"
}
under = {
    "Toy Story" : "Under 18",
    "Frozen"    : "Under 18",
    "Finding Nemo" : "Under 18"
}
age = st.number_input("Enter your age:", step = 1 )

if age >= 18:
    st.write("You are 18 or older. Here are the available 18+ movies:")
    choose = st.selectbox("Select a movie:",   list(above.keys()) )
    age_lim = above[choose]
else:
    st.write("You are under 18. Here are the available Under 18 movies:")
    choose = st.selectbox("Select a movie:",  list(under.keys()))
    age_lim = under[choose]

st.write(f"Selected Movie: {choose} (Rating: {age_lim})")

if st.button("Book Ticket"):
    if age < 18:
        st.error(f"Sorry, you must be at least 18 years old to book '{choose}'.")
    else:
        st.success(f"Ticket booked successfully for '{choose}'! Enjoy the movie.")
