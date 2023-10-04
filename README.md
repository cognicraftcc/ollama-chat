# ollama-chat
Streamlit chat app using LLMs in Ollama docker backend to interact with the difference models available. Now you can access Ollama using a browser with the markdown responses rendered in the display. You can even access it from your phone or tablet once you've installed this on your computer. 

To run:

1. Clone this repository

2. Make sure Docker is installed and run the following
'''
docker-compose up -d
'''
3. If this a new installation, there are no models loaded yet so access the ollama Docker container in terminal mode run the following to pull the orca-mini model for the first time 
'''
ollama pull orca-mini
'''
4. Access from your browser using
'''
http://localhost:8501
'''
5. Load other models of your choice as documented in https://ollama.ai/library


