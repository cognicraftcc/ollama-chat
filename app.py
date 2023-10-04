import streamlit as st 
from langchain.llms import Ollama

st.title(f'🤔🦙 Talk to Ollama AI models')

models=["orca-mini", "codellama", "everythinglm", "llama2-uncensored", "medllama2", "nous-hermes", "open-orca-platypus2", "samantha-mistral", "wizardcoder"]
mymodel = st.selectbox(label="Select a model", options=models, index=0) #default orca-mini

ollama = Ollama(base_url='http://ollama:11434', model=mymodel)


#create storage
if "messages" not in st.session_state:
        st.session_state.messages = []
        
        
# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message.get("role")):
        st.write(message.get("content"))

prompt = st.chat_input('Enter your prompt here!')

if prompt: 
    # Add to storage
    promptModel = f'{mymodel}🤔  {prompt}'
    st.session_state.messages.append({"role": "user","content":promptModel})

    # Display what the user entered
    with st.chat_message("user"):
        st.write(prompt)
                
    response = ollama(prompt)

    # Store and display AI response
    st.session_state.messages.append({"role": "assistant","content":response})    
    with st.chat_message("assistant"):
        st.markdown(response)
    
    
