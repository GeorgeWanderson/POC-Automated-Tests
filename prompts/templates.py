from langchain.prompts import PromptTemplate

def get_prompt_template():
    return PromptTemplate(
        input_variables=["tool", "scenarios"],
        template="""
        Transforme o seguinte cenário de teste em um script de teste automatizado usando {tool}:
        
        Cenário:
        {scenarios}

        Inclua qualquer massa de dados necessária.
        """
    )
