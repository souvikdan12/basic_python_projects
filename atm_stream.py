import streamlit as st


if 'balance' not in st.session_state:
    st.session_state.balance = 50000

if 'pin' not in st.session_state:
    st.session_state.pin = 1234

st.title("ATM   Machine")
p = st.text_input("Enter your PIN:", type="password")

if st.button("Submit"):
    if p.strip().isdigit():
        p = int(p)
    else:
        st.error("Incorrect PIN!")
        st.stop()

    if p == st.session_state.pin:
        st.success("PIN accepted")

        opt = st.selectbox(
            "Choose an option",
            ["Check Balance", "Withdraw", "Deposit", "Exit"]
        )
    
        if opt == "Check Balance":
            if st.button("Show Balance"):
                st.write("Your Balance is :", st.session_state.balance)

        elif opt == "Withdraw":
            w = st.text_input("Amount to withdraw")
            
            if st.button("Withdraw Amount"):
                if w.isdigit():
                    w = int(w)
                    if w <= st.session_state.balance:
                        st.session_state.balance -= w
                        st.success("Withdraw Successful")
                        st.write("Remaining :", st.session_state.balance)
                    else:
                        st.error("Insufficient Balance")
                else:
                    st.error("Invalid Amount")


        elif opt == "Deposit":
            d = st.text_input("Amount to deposit  ")

            if st.button("Deposit Amount"):
                if d.strip().isdigit():
                    d = int(d)
                    st.session_state.balance += d
                    st.success("Deposit Successful")
                    st.write("Updated :", st.session_state.balance)
                else:
                    st.error("Invalid Amount")


        elif opt == "Exit":
            st.write("Thank you for using the ATM!")
            st.stop()
    

    else:
        st.error("Incorrect PIN!")
