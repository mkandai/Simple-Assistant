"""
Author: MK Khodadadi
Latest Modification Date: November 25, 2024
"""

import os
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.output_parsers import OutputFixingParser
from langchain.schema import OutputParserException
from dotenv import load_dotenv
from utils.validation import SushiValidator, ParkingValidator
from utils.prompt import prompt_template

def conversate_with_gpt(
    config: dict, 
    user_choice: str, 
    loaded_dataset: str, 
    user_question: str
) -> dict:
    """
    Function that facilitates a conversation with OpenAI's GPT model using LangChain.
    It generates a prompt based on user input and validates the output using a validator.

    Args:
        config (dict): A dictionary containing configuration settings for the OpenAI model, 
                       including model name and max tokens.
        user_choice (str): A string that determines which validator to use. 
                           Can be either 'sushi' or 'parking'.
        loaded_dataset (str): A dataset or source data to provide context for the GPT model.
        user_question (str): The question or input from the user for which the GPT model will generate a response.

    Returns:
        dict: The parsed and validated output from GPT, either in the form of a Sushi or Parking validator object.
    
    Raises:
        OutputParserException: If parsing the raw output from GPT fails, an exception is raised and 
                               an attempt to fix the output is made.
    """
    # Select appropriate validator based on user choice
    pydantic_object = SushiValidator if user_choice == "sushi" else ParkingValidator

    # Initialize the Pydantic output parser with the selected validator
    parser = PydanticOutputParser(pydantic_object=pydantic_object)

    # Create a prompt template for GPT using the provided prompt template
    prompt = ChatPromptTemplate(
        messages=[
            HumanMessagePromptTemplate.from_template(prompt_template)
        ],
        input_variables=["question", "source_data"],
        partial_variables={
            "format_instructions": parser.get_format_instructions(),
        },
    )

    # Load environment variables from .env file
    load_dotenv()

    # Initialize the GPT model with configuration parameters
    chat_model = ChatOpenAI(
        model=config['openai']['model'],
        max_tokens=config['openai']['max_tokens'],
        openai_api_key=os.environ.get("OPENAI_API_KEY")
    )

    # Format the input prompt with the user's question and the loaded dataset
    _input = prompt.format_prompt(question=user_question, source_data=loaded_dataset)
    
    # Invoke the chat model and obtain raw output
    raw_output = chat_model.invoke(_input.to_messages())
    
    try:
        # Attempt to parse the raw output using the selected parser
        parsed_output = parser.parse(raw_output.content)
    except OutputParserException as e:
        # If parsing fails, print the error and attempt to fix the output
        print(e)
        new_parser = OutputFixingParser.from_llm(
            parser=parser,
            llm=ChatOpenAI()
        )
        # Parse the output using the fixed parser
        parsed_output = new_parser.parse(raw_output.content)

    # Return the parsed output
    return parsed_output
