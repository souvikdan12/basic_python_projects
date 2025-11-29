import streamlit as st

st.set_page_config(page_title="Palindrome Tester") 
st.title("Palindrome Tester")

text_box = st.text_input("Type a word or number")
clicked = st.button("Check Now")

if clicked:
    item = text_box.strip() #trailing spaces hata deta hai
    if not item:
        st.error("You didn't type anything.")
    else:
        temp = item.replace(" ", "").lower()
        flipped = temp[::-1]
        
        if temp == flipped:
            st.success(f"'{item}' reads the same from both sides!")
        else:
            st.error(f"'{item}' is not a palindrome.")
