# Crossword Clue Generator

A Python script that generates crossword puzzle clues and metadata using OpenAI's GPT-4 model.

## Features

- 🧠 AI-powered clue generation using OpenAI's API
- 📖 Generates 2 different short definitions per word
- ⚖️ Assigns difficulty level (1-10) and category for each word
- 💾 Progressive saving to JSON file
- 🔄 Resume capability after interruptions
- 🛠 Error handling with automatic retries

## Prerequisites

- Python 3.x
- OpenAI API key
- `python-dotenv` package

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/crossword-clue-generator.git
cd crossword-clue-generator
```

2. Install required packages:
```bash
pip install openai python-dotenv
```

3. Create a `.env` file in the project root:
```env
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Prepare an input text file with one word per line (e.g., `words.txt`):
```
chat
arbre
ordinateur
...
```

2. Run the script with required parameters:
```bash
python crossword_generator.py --input-file words.txt --output-file clues.json
```

3. To resume from a specific index (e.g., after interruption):
```bash
python crossword_generator.py --input-file words.txt --output-file clues.json --start-from 42
```

## Project Structure

```
crossword-clue-generator/
├── crossword_generator.py  # Main script
├── words.txt               # Sample input file
├── clues.json              # Generated output
├── .env                    # API configuration
└── clues.json.progress     # Progress tracking file
```

## Configuration

Edit the prompt template in the script to modify:
- Definition style
- Difficulty criteria
- Output format

## Error Handling & Resuming

The script automatically:
- Creates a progress file (`.progress`) to track current position
- Saves successfully processed words immediately
- Retries failed API calls
- Handles rate limits with 1-second delays between requests

To resume after interruption:
1. Note the last successfully processed index
2. Run with `--start-from N` where N is the next index

## Sample Output

```json
[
  {
    "word": "chat",
    "description1": "Animal domestique à quatre pattes",
    "description2": "Conversation en ligne",
    "category": "Animaux/Technologie",
    "difficulty": 3
  },
  {
    "word": "arbre",
    "description1": "Végétal ligneux de grande taille",
    "description2": "Représentation graphique en informatique",
    "category": "Nature/Informatique",
    "difficulty": 4
  }
]
```

## Limitations

- Requires OpenAI API credits
- Processing time depends on API rate limits (~1 word/second)
- Generated content should be verified for accuracy
- Cost: Each word uses ~100-150 tokens

## Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

MIT License

---

**Disclaimer**: This project is not affiliated with OpenAI. Generated content may require verification for accuracy. Users are responsible for API usage costs.