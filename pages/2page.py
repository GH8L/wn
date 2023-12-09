import streamlit as st 

# Set the page title
st.title("Hello, Streamlit!")

# Display a header
st.header("Welcome!")

# Get the user's name
name = st.text_input("What is your name?")

# Check if the name is entered and display a personalized hello message
if name:
    st.write(f"Hello, {name.title()}!")
else:
    st.write("Hello, stranger!")

# Display a smaller message
st.subheader("This is my first Streamlit app!")

# Display an image
st.image("https://raw.githubusercontent.com/streamlit/streamlit/main/images/brand/streamlit-logo-primary-col.png")

# Display a button
if st.button("Click me!"):
    st.balloons()

# Display a progress bar
progress = st.progress(0)
for i in range(100):
    # Update the progress bar
    progress.progress(i + 1)
    # Simulate some work
    time.sleep(0.01)

# Display a text block with markdown formatting
st.markdown("""
This is a text block with **markdown formatting**. You can use markdown to format your text, including headings, bold, italics, and lists.
""")

# Display a code block
st.code("""
import streamlit as st

st.title("Hello, Streamlit!")

st.write("This is my first Streamlit app!")
""", language="python")

# Display a chart
import numpy as np
x = np.linspace(0.0, 5.0, 100)
y = np.sin(x)
st.line_chart(y)

# Display a map
st.map(data={"lat": [37.7833], "lon": [-122.4167]})

# Display a file uploader
uploaded_file = st.file_uploader("Upload a file")

# Display a checkbox
agree = st.checkbox("I agree to the terms and conditions.")

# Display a radio button
color = st.radio("Choose a color", ("red", "green", "blue"))

# Display a multiselect
fruits = st.multiselect("Choose your favorite fruits", ("apple", "banana", "orange"))

# Display a slider
age = st.slider("What is your age?", 0, 100)

# Display a date input
date = st.date_input("What is your date of birth?")
