from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver

from src.utils.config import (
    OPENAI_API_KEY,
    OPENAI_API_BASE_URL,
    MODEL_NAME,
    TEMPERATURE
)
from src.tools.search_tools import search_definition, search_examples
from src.tools.vocabulary_tools import generate_vocabulary_test, check_answer

def create_agent():
    """Create and configure the language learning agent."""
    
    # Initialize the language model
    llm = init_chat_model(
        model=MODEL_NAME,
        model_provider="openai",
        api_key=OPENAI_API_KEY,
        base_url=OPENAI_API_BASE_URL,
        temperature=TEMPERATURE
    )
    
    # Create tools list
    tools = [
        search_definition,
        search_examples,
        generate_vocabulary_test,
        check_answer
    ]
    
    # Initialize memory
    memory = MemorySaver()
    
    # Create agent with tools and memory
    agent_executor = create_react_agent(
        llm,
        tools,
        checkpointer=memory
    )
    
    return agent_executor 