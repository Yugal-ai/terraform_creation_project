import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

api_key = os.getenv("api_key")
model = os.getenv("model")



def get_openai_response(prompt:str):    
    prompt_template_strig = f"""
    You are a helpful assistant that generates Terraform code based on user requests.

    User request: {prompt}

    Here are some important guidelines:
    - The code should be valid Terraform code.
    - The code should be well-formatted and easy to read.
    - The code should be complete and ready to be used.
    - The code should not include any comments.
    - The code should not include any explanations.
    - The code should not include any examples.
    - The code should not include any placeholders.
    - The code should not include any unnecessary information.
    - The code should not include any personal information.

    Generate the Terraform code.
    As output, provide only the Terraform code without any additional text or explanation.
    """
    prompt_template = ChatPromptTemplate.from_template(prompt_template_strig)
    prompt = prompt_template.format_messages(input=prompt)
    openai = ChatOpenAI(api_key=api_key)
    response = openai.invoke(prompt)
    print(response.content)
    return response.content

