import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    new = st.session_state.new_todo + "\n"
    todos.append(new)
    functions.write_todos(todos)
    st.session_state.new_todo = ''

st.title('My Todo App')
st.subheader('Todos')

st.write("This app is to increase your productivity")

for i, todo in enumerate(todos):
    checkbox = st.checkbox(todo ,key=todo)
    if checkbox:
        todos.pop(i)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label='Add a task', placeholder='Add a task',
              on_change=add_todo, key='new_todo')

