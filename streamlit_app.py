import streamlit as st
import pty
import subprocess
import os

def execute_command(command):
    master, slave = pty.openpty()
    p = subprocess.Popen(['/bin/sh', '-c', command], stdout=slave, stderr=slave, close_fds=True)
    os.close(slave)
    output = os.read(master, 1024).decode()
    os.close(master)
    return output

# Streamlit app
st.title("Execute Shell Command")

command = st.text_input('Enter a command to execute:')
if command:
    result = execute_command(command)
    st.text_area("Command Output", result)
