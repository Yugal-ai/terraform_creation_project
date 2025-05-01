import streamlit as st
import sys
from pathlib import Path
project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))

from llm_utils.llm_helping_hand import validate_input, query_enhancer
from llm_utils.openai_calls import get_openai_response
from llm_utils.gemini_call import generate_terraform_script_with_gemini

st.set_page_config(page_title="perimattic", page_icon=":cloud:", layout="wide")
sidebar = st.sidebar.title('Cloud Selection...')
options = st.sidebar.radio('Select Cloud Provider', ['AWS', 'Azure', 'GCP'])
instance_type = ""
region = ""

if options == 'AWS':
    region = st.sidebar.selectbox('Select Region', ['us-east-1', 'us-west-2', 'eu-west-1', 'ap-southeast-1'])
    instance_type = st.sidebar.selectbox('Select Instance Type', ['t2.micro', 't2.medium', 't3.large'])
elif options == 'Azure':
    region = st.sidebar.selectbox('Select Location', ['East US', 'West Europe', 'Southeast Asia'])
    instance_type = st.sidebar.selectbox('Select VM Size', ['Standard_B1s', 'Standard_B2s', 'Standard_D2s_v3'])
    
else:
    region = st.sidebar.selectbox('Select Zone', ['us-east1-b', 'us-west1-b', 'europe-west1-b'])
    instance_type = st.sidebar.selectbox('Select Machine Type', ['e2-micro', 'e2-medium', 'n1-standard-1'])
    

st.title("Welcome to our auto terraform creation from perimattic.")

prompt = st.text_area("Enter Terraform specific details here..")
enhanced_prompt = ""
if st.button("Generate Prompt"):
    enhanced_prompt = query_enhancer(prompt , cloud=options, region=region, instance_type=instance_type)
    st.text_area("Enhanced Prompt: ", enhanced_prompt , height=200)
    GENERATED_TERRAFORM = get_openai_response(enhanced_prompt)
    st.text_area("Generated Terraform Script: ", GENERATED_TERRAFORM , height=300)

    if GENERATED_TERRAFORM:
        st.download_button(
            label="Download Terraform Script",
            data=GENERATED_TERRAFORM,
            file_name="generated_terraform_script.tf",
            mime="text/plain"
        )

# if st.button("Generate Terraform Script"):
#     # GENERATED_TERRAFORM = get_openai_response(enhanced_prompt)
#     st.write(enhanced_prompt)
#     # st.text_area("Generated Terraform Script: ", GENERATED_TERRAFORM , height=300)
        



