import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

gemini_api_key = os.getenv("gemnini_api_key")
genai.configure(api_key=gemini_api_key)

def generate_terraform_script_with_gemini(user_query):
    """
    Generates a Terraform script using the Gemini LLM based on a user's query.

    Args:
        user_query: A string representing the user's request.

    Returns:
        A string containing the generated Terraform script, or an error message.
    """

    model = genai.GenerativeModel('gemini-2.5-pro-exp-03-25')  # Use gemini-pro. You may need to change this based on the model you have access to.

    prompt = f"""
    You are a helpful assistant that generates Terraform code based on user requests.

    User request: {user_query}

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

    try:
        response = model.generate_content(prompt)
        terraform_code = response.text.strip() #remove leading and trailing whitespace.
        return terraform_code
    except Exception as e:
        return f"An error occurred: {e}"


