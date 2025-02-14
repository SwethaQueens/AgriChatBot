import streamlit as st
from databasecon import connection
def signup_page():
    st.title("Signup Page")
    
    # Signup Form
    new_username = st.text_input("New Username")
    email = st.text_input("Enter Email")
    mobile = st.text_input("Enter Mobile Number")
    new_password = st.text_input("New Password", type="password")
    cn_password = st.text_input("Confirm Password", type="password")
    signup_button = st.button("Signup")
    sql ="insert into user(username,email,mobile,password) values (%s,%s,%s,%s)"
    val =(new_username,email,mobile,new_password)
    if signup_button:
        # Replace with your signup logic (e.g., save to a database)
        if cn_password == new_password:
            # Save to database
            conn,cur = connection()
            cur.execute(sql,val)
            conn.commit()
            if cur.rowcount >= 1:
                st.success("Account created successfully! Please log in.")
            else:
                st.error("Failed to create account")
        else:
            st.error("Missmatch password .")
