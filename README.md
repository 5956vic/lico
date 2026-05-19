# 🎭 Random Joke Generator

A fun random joke generator that fetches jokes from an external API. Available in multiple formats: Node.js, Python, and interactive web interface.

## Features

✨ **Multiple Formats**
- 🟨 JavaScript/Node.js version
- 🐍 Python version
- 🌐 Interactive Web Interface

🎯 **Joke Categories**
- General
- Programming
- Knock-Knock
- Dark
- Spooky
- Any (random)

🚀 **Capabilities**
- Single joke fetching
- Batch joke fetching (get multiple jokes at once)
- Error handling and validation
- Beautiful responsive UI

## API Used

This project uses the free [JokeAPI](https://jokeapi.dev/) which provides a wide variety of jokes with no authentication required.

## Installation & Usage

### JavaScript/Node.js

**Requirements:** Node.js installed

```bash
node joke-generator.js
```

**Output:**
```
🎭 Random Joke Generator

Fetching a random joke...

==================================================
Why do Java developers wear glasses?
Because they don't C#
==================================================

Category: Programming
```

### Python

**Requirements:** Python 3.6+ and `requests` library

```bash
# Install dependencies
pip install requests

# Run the generator
python joke-generator.py
```

**Output:**
```
🎭 Random Joke Generator

Fetching a random joke...

==================================================
Setup: Why did the scarecrow win an award?
Punchline: He was outstanding in his field!
==================================================

Category: General
```

### Web Interface

Simply open `joke-generator.html` in your web browser.

**Features:**
- Select joke category from dropdown
- Single joke or 3 jokes at once
- Real-time joke counter
- Beautiful gradient UI with animations
- Fully responsive design

## Project Structure

```
.
├── joke-generator.js      # Node.js implementation
├── joke-generator.py      # Python implementation
├── joke-generator.html    # Web interface
└── README.md              # This file
```

## Examples

### Using as a Module (JavaScript)

```javascript
const { getJoke, displayJoke } = require('./joke-generator.js');

async function main() {
  try {
    const joke = await getJoke('Programming');
    displayJoke(joke);
  } catch (error) {
    console.error('Error:', error);
  }
}

main();
```

### Using as a Module (Python)

```python
from joke_generator import get_joke, display_joke, get_multiple_jokes

# Single joke
joke = get_joke('General')
display_joke(joke)

# Multiple jokes
jokes = get_multiple_jokes(count=5, category='Programming')
for joke in jokes:
    display_joke(joke)
```

## Error Handling

All implementations include proper error handling:
- Network timeouts
- API errors
- JSON parsing errors
- Invalid categories

## API Response Format

Single Joke:
```json
{
  "error": false,
  "category": "General",
  "type": "single",
  "joke": "Why don't scientists trust atoms? Because they make up everything!"
}
```

Two-Part Joke:
```json
{
  "error": false,
  "category": "Programming",
  "type": "twopart",
  "setup": "Why do Java developers wear glasses?",
  "delivery": "Because they don't C#"
}
```

## Performance

- **API Response Time:** ~200-500ms
- **Batch Fetching:** Parallel requests for faster loading
- **No Rate Limiting:** JokeAPI is free and has generous limits

## License

MIT License - Feel free to use and modify!

## Credits

- Jokes provided by [JokeAPI](https://jokeapi.dev/)
- Built with ❤️

## Troubleshooting

### "Failed to fetch joke" error
- Check your internet connection
- Verify the API is accessible at https://v2.jokeapi.dev/joke
- Try a different joke category

### Python ImportError for requests
```bash
pip install --upgrade requests
```

### Web interface not loading jokes
- Check browser console for CORS errors
- Ensure JavaScript is enabled
- Try a different category

## Contributing

Feel free to fork, modify, and improve this project! Some ideas:
- Add more API sources
- Implement caching
- Add joke filtering options
- Create additional UI themes
