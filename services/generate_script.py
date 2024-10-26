from langchain.llms import OpenAI
from langchain.chains import LLMChain
from prompts.templates import get_prompt_template

def generate_script(tool, scenarios):
    prompt = get_prompt_template()
    llm = OpenAI(temperature=0.5)
    chain = LLMChain(llm=llm, prompt=prompt)
    
    try:
        result = chain.run(tool=tool, scenarios=scenarios)
        test_data = "Exemplo de massa de dados gerado pela IA."
        return result, test_data
    except Exception as e:
        return f"Erro ao gerar o script: {e}", ""
