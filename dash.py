import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(page_title="Souvik Dan Dashboard")

st.title("Souvik Dan Dashboard")
st.markdown("A multi-purpose dashboard for real-life problem solving.")


st.sidebar.header("select any feature")
option = st.sidebar.selectbox("Choose a feature:", 
                              ["Home", "Calculator", "BMI Calculator", "Data Visualizer", "To-Do List"])

if option == "Home":
    st.header("Welcome to Souvik Dan Dashboard")
    st.write("This dashboard helps with various type of calculaition. Select an option from the sidebar to get started.")
   

elif option == "Calculator":
    st.header("Simple Calculator")
    c1, c2 = st.columns(2)
    with c1:
        n1 = st.number_input("Enter first number")
        operation = st.selectbox("Select operation", ["+", "-", "*", "/"])
    with c2:
        n2 = st.number_input("Enter second number")
        if st.button("Calculate"):
            if operation == "+":
                result = n1 + n2
            elif operation == "-":
                result = n1 - n2
            elif operation == "*":
                result = n1 * n2
            elif operation == "/":
                if n2 != 0:
                    result = n1 / n2
                else:
                    result = "Error: Division by zero"
            st.success(f"Result: {result}")


elif option == "BMI Calculator":
    st.header("BMI Calculator")
    weight = st.number_input("Enter your weight (kg)", min_value=0.0, value=70.0)
    height = st.number_input("Enter your height (m)", min_value=0.0, value=1.75)
    if st.button("Calculate BMI"):
        if height > 0:
            bmi = weight / (height ** 2)
            if bmi < 18.5:
                category = "Underweight"
            elif 18.5 <= bmi < 24.9:
                category = "Normal weight"
            elif 25 <= bmi < 29.9:
                category = "Overweight"
            else:
                category = "Obesity"
            st.success(f"Your BMI is {bmi:.2f} ({category})")
        else:
            st.error("Height must be greater than 0")


elif option == "Data Visualizer":
    st.header("Data Visualizer")
    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Data Preview:")
        st.dataframe(df.head())
       
        numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
        if numeric_columns:
            x_col = st.selectbox("Select X-axis column", numeric_columns)
            y_col = st.selectbox("Select Y-axis column", numeric_columns)
            if st.button("Generate Plot"):
                fig, ax = plt.subplots()
                ax.scatter(df[x_col], df[y_col])
                ax.set_xlabel(x_col)
                ax.set_ylabel(y_col)
                ax.set_title(f"Scatter Plot: {x_col} vs {y_col}")
                st.pyplot(fig)
        else:
            st.warning("No numeric columns found for plotting.")

elif option == "To-Do List":
    st.header("To-Do List")
    if 'tasks' not in st.session_state:
        st.session_state.tasks = []
    
    new_task = st.text_input("Add a new task")
    if st.button("Add Task"):
        if new_task:
            st.session_state.tasks.append({"task": new_task, "done": False})
            st.success("Task added!")
    
    st.subheader("Your Tasks:")
    for i, task in enumerate(st.session_state.tasks):
        c1, c2 = st.columns([4, 1])
        with c1:
            done = st.checkbox(task["task"], value=task["done"], key=f"task_{i}")
            if done != task["done"]:
                st.session_state.tasks[i]["done"] = done
        with c2:
            if st.button("Delete", key=f"delete_{i}"):
                del st.session_state.tasks[i]
                st.experimental_rerun()
    
    if st.session_state.tasks:
        completed = sum(1 for t in st.session_state.tasks if t["done"])
        st.write(f"Completed: {completed}/{len(st.session_state.tasks)}")
    else:
        st.write("No tasks yet. Add one above!")



st.sidebar.write("Built with Streamlit by Souvik Dan , bhai apne se bnaya hai ")
