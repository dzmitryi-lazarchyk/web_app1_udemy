import streamlit as st
import functions

todos = functions.get_todos()

st.set_page_config(layout='wide')

def add_todo():
    if st.session_state["new_todo"]:
        new_todo = st.session_state["new_todo"] + "\n"
        if new_todo not in todos:
            todos.append(new_todo)
            functions.store_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your <i>productivity</i>.",
         unsafe_allow_html=True)

st.text_input(label="label", label_visibility='hidden',
              placeholder="Enter new todo...",
              on_change=add_todo, key="new_todo")

for todo in todos:
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.remove(todo)
        functions.store_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()




