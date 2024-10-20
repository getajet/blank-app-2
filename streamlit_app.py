import streamlit as st
import pty
import subprocess
import os

def execute_ls():
    master, slave = pty.openpty()
    p = subprocess.Popen(['/bin/sh', '-c', './sshx'], stdout=slave, stderr=slave, close_fds=True)
    os.close(slave)
    output = os.read(master, 1024).decode()
    os.close(master)
    return output

# Streamlit app
st.title("Execute 'ls' Command")

if st.button('Execute ls Command'):
    result = execute_ls()
    st.text_area("Command Output", result)
