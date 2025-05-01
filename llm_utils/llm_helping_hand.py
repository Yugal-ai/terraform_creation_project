import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel,Field

load_dotenv()


# class Structure_output(BaseModel):
#     """ LLM Output with Structure outoput as a valid terraform script"""
#     terraform_script = Field(description="Valid Terraform script with interndation and resourse allign without any error while execution")


llm = ChatOpenAI()
# structure_llm = llm.with_structured_output(Structure_output)
def validate_input(prompt:str):
    if prompt:
        resp = llm.invoke(f"You are an expert in the Infrastructure as code domain. You are helping a user to create a terraform script for deploying  in the cloud. The user has selected the cloud provider. Validate if the given user has enterred the valid Terraform specific or not {prompt}, respond me in True or False only")
        return resp.content    
    else:
        return False

def query_enhancer(query: str, cloud: str, region: str, instance_type: str) -> str:
    template_string = f"""You are a highly skilled AI assistant specializing in Terraform script generation. 
    Your task is to enhance the user's query to make it more specific, detailed, and aligned with global best practices 
    and security standards for Infrastructure as Code (IaC). Act as an expert in cloud infrastructure and security.

    The user has selected the following details:
    - Cloud Provider: {cloud}
    - Region: {region}
    - Instance Type: {instance_type}

    The user's query is: "{query}"

    Your response should:
    1. Be written in a professional tone suitable for an experienced IaC engineer.
    2. Include all necessary resources, providers, and configurations required to fulfill the user's request.
    3. Follow global best practices for Terraform and cloud infrastructure.
    4. Incorporate security considerations, such as:
       - Configuring secure access (e.g., SSH keys, IAM roles, or service accounts).
       - Restricting access to sensitive resources using security groups, firewalls, or access control lists.
       - Enforcing encryption for data at rest and in transit.
       - Using least privilege principles for permissions.
    5. Ensure scalability, reliability, and cost-efficiency where applicable.
    6. Provide a clear and concise description of the Terraform script's purpose.

    Examples of enhanced queries:
    - User Query: "I want to set up an application built in AngularJS/Next.js and deploy it on AWS. Can you do that for me?"
      Enhanced Query: "Write a Terraform script to deploy an AngularJS/Next.js application on AWS. The script should include the following resources: 
      an EC2 instance for hosting the application, an S3 bucket for static files, and an RDS instance for the database. Ensure the EC2 instance is 
      accessible via a public IP address with security groups configured to allow HTTP and HTTPS traffic. Use IAM roles for secure access to AWS 
      resources, enable encryption for the RDS database, and configure auto-scaling for the EC2 instance to handle traffic spikes."

    - User Query: "I have an auto-scaling Node.js application and want to deploy APIs for it. Can you do that for me?"
      Enhanced Query: "Write a Terraform script to deploy a Node.js application with auto-scaling capabilities. The script should include the following 
      resources: EC2 instances, an Application Load Balancer, and a security group. Configure the load balancer to distribute traffic across instances 
      and enable HTTPS for secure communication. Include auto-scaling policies based on CPU utilization. Ensure the security groups allow only HTTP and 
      HTTPS traffic, and use IAM roles for secure access to AWS resources."

    Based on the user's query and the provided details, generate an enhanced query that meets these requirements. Respond with the enhanced query only, 
    without any additional explanation or text.
    """
    prompt_template = ChatPromptTemplate.from_template(template_string)
    prompt = prompt_template.format_messages(query=query)
    response = llm.invoke(prompt)
    return response.content


    
