import streamlit as st
from services.generate_script import generate_script
from config.settings import openai  # Assegura que a API Key foi carregada

# Interface da POC
st.title("POC - Transformação de Cenários de Teste em Script Automatizado")

# Campo de entrada para o cenário de teste
scenarios_input = st.text_area(
    "Insira os cenários de teste:", 
    height=200, 
    placeholder="Exemplo:\nDado que o usuário está na página de login\nQuando o usuário insere credenciais válidas\nEntão o usuário é redirecionado para a página inicial."
)

# Select box para escolher a ferramenta de automação
tool_choice = st.selectbox(
    "Escolha a ferramenta de automação:",
    ["Robot Framework", "Selenium WebDriver", "Cypress"]
)

# Botão para gerar o script
if st.button("Gerar Script de Automação"):
    if scenarios_input.strip() == "":
        st.warning("Por favor, insira pelo menos um cenário de teste.")
    else:
        # Chamada da função para gerar script
        generated_script, test_data = generate_script(tool_choice, scenarios_input)

        # Exibição do script e massa de dados gerados
        st.subheader("Script de Automação:")
        st.code(generated_script, language="python" if tool_choice == "Selenium WebDriver" else "robot" if tool_choice == "Robot Framework" else "javascript")

        st.subheader("Massa de Dados:")
        st.write(test_data)
