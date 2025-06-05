# English Language Learning Assistant

An AI-powered English language learning assistant that helps users understand words and improve their vocabulary through interactive features.

## Features

- Word definitions from multiple dictionaries (Oxford and Merriam-Webster)
- Comprehensive definition combining
- Vocabulary testing with difficulty levels
- Answer checking and feedback
- Interactive chat interface

## Usage

1. Run the application:
```bash
python src/main.py
```

2. Open your web browser and navigate to the URL shown in the terminal (usually http://localhost:7860)

3. Start interacting with the assistant:
   - Ask for word definitions
   - Request vocabulary tests
   - Get feedback on your answers

## Project Structure

```
project/
├── src/
│   ├── tools/
│   │   ├── dictionary_tools.py
│   │   └── vocabulary_tools.py
│   ├── core/
│   │   └── agent.py
│   ├── ui/
│   │   └── gradio_interface.py
│   ├── utils/
│   │   └── config.py
│   └── main.py
├── tests/
├── requirements.txt
└── README.md
```
