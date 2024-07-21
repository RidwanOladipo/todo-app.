import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


# st.title("My Todo App")
# st.subheader("This is my todo app.")
# st.write("This app is to increase your productivity.")
# st.title("My Todo App")
st.title("Productivity HQ!")
st.subheader("Your one-stop spot for crushing your to-do list.")
st.write("<em>Organize your <b>tasks</b>, smash your <b>goals</b>, and feel the satisfaction of <b>achievement</b>. "
         "We'll help you conquer your day, <b>one to-do at a time</b>!</em>", unsafe_allow_html=True)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        # print(checkbox)
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo")

