"""
Author: MK Khodadadi
Latest Modification Date: November 25, 2024
"""

import os
import yaml
import json
from typing import Dict, Any

from utils.conversation_module import conversate_with_gpt

def main() -> None:
    """
    The main function for the Simple Assistant program.
    
    This program interacts with the user, allowing them to search for sushi or parking 
    places nearby, and ask questions about those places. It loads configuration from 
    a YAML file and places data from JSON files. It interacts with the user in a loop 
    and processes their requests until the user types 'quit'.

    The assistant uses a conversational AI model (via `conversate_with_gpt`) to answer 
    user questions about the selected places.
    
    The program expects the following file structure:
    - settings/config.yaml: The configuration file.
    - places-data/{sushi.json, parking.json}: Data files for places.
    
    Returns:
        None: This function runs an interactive session and does not return any value.
    """
    
    print(f"{30*'='} Simple Assistant {30*'='}")

    MAIN_PATH = os.path.abspath('.')
    SETTINGS_PATH = os.path.join(MAIN_PATH, "settings/config.yaml")
    DATA_PATH = os.path.join(MAIN_PATH, 'places-data')

    # Load configuration from YAML file
    config: Dict[str, Any] = yaml.safe_load(open(SETTINGS_PATH))

    while True:
        user_choice: str = input("Would you like to search for sushi or parking? (type 'quit' to exit): ").lower()
        
        if user_choice == "quit":
            print("Goodbye!")
            break
        
        if user_choice not in ["sushi", "parking"]:
            print("Invalid input. Please enter 'sushi' or 'parking'.")
            continue

        # Load dataset based on user choice (sushi or parking)
        loaded_dataset: list[Dict[str, str]] = json.load(open(os.path.join(DATA_PATH, f'{user_choice}.json')))

        print(f"Here are the nearby {user_choice}s:")
        for place in loaded_dataset:
            print(f"- {place['title']}")
        
        user_question: str = input("What would you like to ask about these places? ")
        
        # Get response from the assistant using the loaded data and user's question
        response: str = conversate_with_gpt(
            config=config,
            user_choice=user_choice,
            loaded_dataset=loaded_dataset,
            user_question=user_question
        )

        print("ASSISTANT: ", response)

if __name__ == "__main__":
    main()
