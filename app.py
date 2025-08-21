import streamlit as st
from different_datatype import describe_File
st.set_page_config(page_title="AI File Describer",page_icon="🤖")
st.title("AI File Describer")
st.write("Upload a file (image, video, pdf etc) and I'll describe it!")
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file:
    content = describe_File(uploaded_file)
    st.subheader("File Description")
    st.write(content)
