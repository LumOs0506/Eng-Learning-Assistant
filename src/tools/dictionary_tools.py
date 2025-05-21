import requests
from typing import Dict, List
from langchain_core.tools import tool
from ..utils.config import (
    OXFORD_API_KEY,
    OXFORD_APP_ID,
    MERRIAM_WEBSTER_API_KEY,
    MAX_DEFINITIONS
)

@tool
def oxford_dictionary(word: str) -> str:
    """Look up a word in Oxford Dictionary API.
    
    Args:
        word (str): The word to look up
        
    Returns:
        str: Formatted definition from Oxford Dictionary
    """
    try:
        url = f"https://od-api.oxforddictionaries.com/api/v2/entries/en/{word.lower()}"
        headers = {
            "app_id": OXFORD_APP_ID,
            "app_key": OXFORD_API_KEY
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        data = response.json()
        definitions = []
        
        for result in data.get("results", [])[:MAX_DEFINITIONS]:
            for lexical_entry in result.get("lexicalEntries", []):
                for entry in lexical_entry.get("entries", []):
                    for sense in entry.get("senses", []):
                        if "definitions" in sense:
                            definitions.extend(sense["definitions"])
        
        if not definitions:
            return f"No definitions found for '{word}' in Oxford Dictionary."
            
        formatted_definitions = "\n".join([f"{i+1}. {defn}" for i, defn in enumerate(definitions)])
        return f"Oxford Dictionary definitions for '{word}':\n{formatted_definitions}"
        
    except requests.exceptions.RequestException as e:
        return f"Error accessing Oxford Dictionary API: {str(e)}"

@tool
def merriam_webster(word: str) -> str:
    """Look up a word in Merriam-Webster Dictionary API.
    
    Args:
        word (str): The word to look up
        
    Returns:
        str: Formatted definition from Merriam-Webster Dictionary
    """
    try:
        url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}"
        params = {"key": MERRIAM_WEBSTER_API_KEY}
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        data = response.json()
        definitions = []
        
        for entry in data[:MAX_DEFINITIONS]:
            if isinstance(entry, dict) and "shortdef" in entry:
                definitions.extend(entry["shortdef"])
        
        if not definitions:
            return f"No definitions found for '{word}' in Merriam-Webster Dictionary."
            
        formatted_definitions = "\n".join([f"{i+1}. {defn}" for i, defn in enumerate(definitions)])
        return f"Merriam-Webster Dictionary definitions for '{word}':\n{formatted_definitions}"
        
    except requests.exceptions.RequestException as e:
        return f"Error accessing Merriam-Webster Dictionary API: {str(e)}"

@tool
def combine_definitions(word: str) -> str:
    """Combine definitions from multiple dictionaries into a comprehensive response.
    
    Args:
        word (str): The word to look up
        
    Returns:
        str: Combined and formatted definitions from all available dictionaries
    """
    oxford_def = oxford_dictionary(word)
    merriam_def = merriam_webster(word)
    
    combined = f"Comprehensive definitions for '{word}':\n\n"
    combined += f"{oxford_def}\n\n"
    combined += f"{merriam_def}"
    
    return combined 