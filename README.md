# English Language Learning Assistant

An AI-powered English language learning assistant that helps users understand words and improve their vocabulary through interactive features.

## Features

- Word definitions from multiple dictionaries (Oxford and Merriam-Webster)
- Comprehensive definition combining
- Vocabulary testing with difficulty levels
- Answer checking and feedback
- Interactive chat interface

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with your API keys:
```
OPENAI_API_KEY=your-openai-api-key
OPENAI_API_BASE_URL=https://api.chatanywhere.tech/
OXFORD_API_KEY=your-oxford-api-key
OXFORD_APP_ID=your-oxford-app-id
MERRIAM_WEBSTER_API_KEY=your-merriam-webster-api-key
```

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

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 