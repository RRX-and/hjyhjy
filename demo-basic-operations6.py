import streamlit as st
st.title('Hello 2208!')
st.header('好累tired')
st.subheader('all days tired~~~')
st.text('好多小组作业~~好多字的论文~~~')
st.markdown('this is an image: ![Alt Text](https://tse1-mm.cn.bing.net/th/id/OIP-C.Rmu2HNfPTot9nN9kWt0dbgHaNK?w=106&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7)')
if st.checkbox("Show/Hide"):
    st.text("You checked the box")
    
status=st.radio("select gender:",
                ("Male",
                 "Female"))
if status == "Male":
    st.success("Male")
else:
    st.success("Female")
    
if status == "Male":
    st.success("Male")
else:
    st.success("Female")

hobbies=st.multiselect("Hobbies:",
               ['Reading','Writing','Coding','Traveling'])
st.write("You selected:",hobbies)


if st.button("about"):
    st.text("Streamlit is a great tool")

name=st.text_input("Enter your name")
if st.button("Submit"):
    st.write("Hello,",'', name)
level=st.slider("select your level",1,5)
st.write("your selected:",level)