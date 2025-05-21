import random
from typing import List, Dict, Tuple
from langchain_core.tools import tool
from .search_tools import search_definition, search_examples

# Sample word lists by difficulty (you can expand these)
EASY_WORDS = ["happy", "book", "run", "eat", "sleep", "walk", "talk", "read", "write", "play"]
MEDIUM_WORDS = ["eloquent", "perseverance", "ambiguous", "pragmatic", "resilient", "meticulous", "tenacious", "versatile", "diligent", "astute"]
HARD_WORDS = ["quixotic", "perspicacious", "obfuscate", "pernicious", "ineffable", "ephemeral", "ubiquitous", "serendipity", "mellifluous", "inexorable"]

@tool
def generate_vocabulary_test(difficulty: str = "medium") -> str:
    """Generate a vocabulary test based on difficulty level.
    
    Args:
        difficulty (str): The difficulty level ('easy', 'medium', or 'hard')
        
    Returns:
        str: A word to test the user's vocabulary
    """
    difficulty = difficulty.lower()
    word_list = {
        "easy": EASY_WORDS,
        "medium": MEDIUM_WORDS,
        "hard": HARD_WORDS
    }.get(difficulty, MEDIUM_WORDS)
    
    word = random.choice(word_list)
    return f"Please define the word: {word}"

@tool
def check_answer(word: str, user_answer: str) -> str:
    """Check user's answer against search results.
    
    Args:
        word (str): The word being tested
        user_answer (str): The user's definition attempt
        
    Returns:
        str: Feedback on the user's answer
    """
    # Get definitions from search
    definition_results = search_definition(word)
    example_results = search_examples(word)
    
    # Simple keyword matching (can be improved with more sophisticated NLP)
    keywords = set(word.lower().split())
    user_keywords = set(user_answer.lower().split())
    
    # Calculate similarity score (very basic implementation)
    common_keywords = keywords.intersection(user_keywords)
    similarity_score = len(common_keywords) / len(keywords) if keywords else 0
    
    feedback = f"Word: {word}\n\n"
    feedback += f"Your answer: {user_answer}\n\n"
    feedback += f"Search results:\n{definition_results}\n\n"
    feedback += f"Example usage:\n{example_results}\n\n"
    
    if similarity_score > 0.7:
        feedback += "Great job! Your definition is very close to the correct meaning."
    elif similarity_score > 0.4:
        feedback += "Good attempt! Your definition captures some aspects of the word's meaning."
    else:
        feedback += "Try again! Your definition might need some improvement."
    
    return feedback 