import uuid
import gradio as gr
from langchain_core.messages import HumanMessage, AIMessage

from src.core.agent import create_agent

def create_chat_interface():
    """Create and launch the Gradio chat interface."""
    
    # Create the agent
    agent_executor = create_agent()
    
    def chat(message, history, thread_id):
        """Handle chat interactions with the agent."""
        # Create a new thread id if not already present
        if not thread_id:
            thread_id = str(uuid.uuid4())
        
        # Set up the config using the session-specific thread id
        config = {"configurable": {"thread_id": thread_id}}
        
        # Append the user's message and a placeholder for the bot's response
        history = history + [(message, "")]
        response_index = len(history) - 1
        
        full_response = ""
        # Stream the output from the backend
        for chunk, metadata in agent_executor.stream(
            {"messages": [HumanMessage(message)]},
            config,
            stream_mode="messages",
        ):
            if isinstance(chunk, AIMessage):
                full_response += chunk.content
                # Update the chat history with the new partial response
                history[response_index] = (message, full_response)
                # Yield the updated chat history
                yield history, thread_id, ""
    
    # Build the Gradio interface
    with gr.Blocks(theme=gr.themes.Soft()) as demo:
        gr.Markdown("""
        # English Language Learning Assistant
        Welcome! I can help you:
        - Look up word definitions
        - Take vocabulary tests
        - Improve your English skills
        
        Just type your message below to get started!
        """)
        
        # State component for thread id
        thread_state = gr.State()
        
        # Chat interface components
        chatbot = gr.Chatbot(height=600)
        with gr.Row():
            msg_input = gr.Textbox(
                placeholder="Type your message here...",
                show_label=False,
                container=False
            )
            send_btn = gr.Button("Send", variant="primary")
        
        # Clear button
        clear_btn = gr.Button("Clear Chat")
        
        # Event handlers
        send_btn.click(
            chat,
            inputs=[msg_input, chatbot, thread_state],
            outputs=[chatbot, thread_state, msg_input]
        )
        
        msg_input.submit(
            chat,
            inputs=[msg_input, chatbot, thread_state],
            outputs=[chatbot, thread_state, msg_input]
        )
        
        clear_btn.click(
            lambda: ([], None, ""),
            inputs=[],
            outputs=[chatbot, thread_state, msg_input]
        )
    
    return demo

def launch_interface():
    """Launch the Gradio interface."""
    demo = create_chat_interface()
    demo.launch(share=True) 