# Simple Assistant

A simple interactive assistant that helps users search for nearby sushi or parking places, and provides answers to user queries about these places. The assistant loads configuration and data from files and utilizes a conversational AI model to respond to questions.

## Features

- Search for nearby sushi restaurants or parking spots.
- Ask questions about the listed places (e.g., details, reviews, etc.).
- Interactive console interface.
- Configurable settings loaded from a YAML file.
- Data for sushi and parking places loaded from separate JSON files.

## Requirements

You can install the required libraries using `pip`:

```bash
pip install -r requirements.txt
```

## Project Structure

The project expects the following file structure:

```
Simple-Assistant/
│
├── settings/
│   └── config.yaml              # Configuration file for the assistant
│
├── places-data/
│   ├── sushi.json               # Data for sushi places (a JSON file)
│   └── parking.json             # Data for parking places (a JSON file)
│
├── utils/
│   ├── conversation_module.py   # Modules for invoking the LLM
│   ├── prompt.py                # Prompt template
│   └── validation.py            # Data structure for data validation
│
└── main.py                      # Main program file (Simple Assistant)
```

## Getting Started

- Clone the repository or download the code.
- Make sure you have the required dependencies installed.
- Prepare the config.yaml file with the necessary configuration.
- Run the program:
```bash
python main.py
```
