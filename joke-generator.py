#!/usr/bin/env python3

import requests
import random
import json
from typing import Dict, Optional

JOKE_API_URL = "https://v2.jokeapi.dev/joke"
CATEGORIES = ["Any", "General", "Programming", "Knock-Knock", "Dark", "Spooky"]

def get_joke(category: str = "Any") -> Dict:
    """
    Fetch a random joke from JokeAPI.
    
    Args:
        category: Joke category (General, Programming, Knock-Knock, etc.)
        
    Returns:
        Dictionary containing joke data
        
    Raises:
        requests.RequestException: If API call fails
        ValueError: If API returns an error
    """
    try:
        url = f"{JOKE_API_URL}/{category}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        
        joke = response.json()
        
        if joke.get('error'):
            raise ValueError(f"API Error: {joke.get('message', 'Unknown error')}")
            
        return joke
    except requests.RequestException as e:
        raise requests.RequestException(f"Failed to fetch joke: {e}")

def display_joke(joke: Dict) -> None:
    """
    Format and display a joke.
    
    Args:
        joke: Joke dictionary from API
    """
    print("\n" + "=" * 50)
    
    if joke.get('type') == 'single':
        print(joke.get('joke', 'No joke content'))
    else:
        print(f"Setup: {joke.get('setup', 'N/A')}")
        print(f"\nPunchline: {joke.get('delivery', 'N/A')}")
    
    print("=" * 50 + "\n")

def get_multiple_jokes(count: int = 3, category: str = "Any") -> list:
    """
    Fetch multiple jokes.
    
    Args:
        count: Number of jokes to fetch
        category: Joke category
        
    Returns:
        List of joke dictionaries
    """
    jokes = []
    for i in range(count):
        try:
            joke = get_joke(category)
            jokes.append(joke)
        except Exception as e:
            print(f"Error fetching joke {i+1}: {e}")
    return jokes

def main():
    """
    Main function to run the joke generator.
    """
    print("🎭 Random Joke Generator\n")
    print("Fetching a random joke...")
    
    try:
        category = random.choice(CATEGORIES)
        joke = get_joke(category)
        display_joke(joke)
        print(f"Category: {category}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()