from duckduckgo_search import DDGS
from langchain_core.tools import tool
from ..utils.config import MAX_SEARCH_RESULTS

@tool
def search_definition(word: str) -> str:
    """Search for word definitions using DuckDuckGo.
    
    Args:
        word (str): The word to look up
        
    Returns:
        str: Formatted search results with definitions
    """
    try:
        # Search for definitions
        results = list(DDGS().text(f"define {word}", max_results=MAX_SEARCH_RESULTS))
        
        if not results:
            return f"No definitions found for '{word}'."
        
        # Format the results
        formatted_results = []
        for i, result in enumerate(results, 1):
            title = result.get("title", "No title")
            snippet = result.get("body", "No snippet")
            formatted_results.append(
                f"Result {i}:\nTitle: {title}\nDefinition: {snippet}\n"
            )
        
        return f"Definitions for '{word}':\n\n" + "\n".join(formatted_results)
        
    except Exception as e:
        return f"Error searching for definition: {str(e)}"

@tool
def search_examples(word: str) -> str:
    """Search for example sentences using the word.
    
    Args:
        word (str): The word to find examples for
        
    Returns:
        str: Formatted search results with example sentences
    """
    try:
        # Search for example sentences
        results = list(DDGS().text(f"example sentences with {word}", max_results=MAX_SEARCH_RESULTS))
        
        if not results:
            return f"No example sentences found for '{word}'."
        
        # Format the results
        formatted_results = []
        for i, result in enumerate(results, 1):
            title = result.get("title", "No title")
            snippet = result.get("body", "No snippet")
            formatted_results.append(
                f"Example {i}:\nContext: {title}\nSentence: {snippet}\n"
            )
        
        return f"Example sentences for '{word}':\n\n" + "\n".join(formatted_results)
        
    except Exception as e:
        return f"Error searching for examples: {str(e)}" 