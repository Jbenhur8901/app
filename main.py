import streamlit as st
import yanola as yl
import requests as re


with st.sidebar:
   st.write("# Options")
   st.markdown("---")
   index = st.text_input("Entrez le nom de l'index")
   subject = st.text_input("Entrez le thème principal")
   sys_instructions = st.text_area("Entrez vos instructions")
   

st.title("💬 Yanola")
st.caption("🚀 Interface utilisateur")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Bonjour je suis yanola, comment puis je vous aider ?"}]

if "chat_id" not in st.session_state :

    st.session_state["chat_id"] = yl.generate_id()


for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input(placeholder="Message à Yanola"):

    yl = yl.RetrievalAgent(prompt, index,sys_instructions,st.session_state["chat_id"],subject)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    msg = yl.run_agent()
    
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write_stream(yl.stream_data)
    
