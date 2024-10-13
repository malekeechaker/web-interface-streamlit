from langchain_community.llms import Ollama
from langchain.prompts import ChatPromptTemplate
import streamlit as st

st.title("Chatbot basé sur LLaMA2")

user_input = st.text_input("Posez une question :")

# Utilisez un modèle différent qui est sûr d'être installé
model = Ollama(model="llama2", base_url="http://localhost:11434")

# Modification de l'initialisation de ChatPromptTemplate
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "Vous êtes un assistant utile."),
    ("user", "Question: {question}")
])

def generate_response(question):
    prompt = prompt_template.format(question=question)
    response = model.invoke(prompt)
    return response

if user_input:
    try:
        response = generate_response(user_input)
        st.write(response)
    except Exception as e:
        st.error(f"Une erreur s'est produite: {str(e)}")
