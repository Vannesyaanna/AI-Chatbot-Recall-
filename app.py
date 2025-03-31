import gradio as gr
import random

# Expanded English response database
responses = {
    # Greetings
    "hi": ["Hey there!", "Hello! How can I help?", "Hi! Nice to meet you!"],
    "hello": ["Hello! What's up?", "Hey! How are you today?", "Hi there! 😊"],
    
    # How are you?
    "how are you": [
        "I'm great, thanks for asking!",
        "Doing well! How about you?",
        "Just chilling like a villain! 😎"
    ],
    
    # Name/Identity
    "your name": [
        "I'm SimpleBot, your friendly AI!",
        "Call me Recall! 🤖",
        "I'm an AI without a name... call me whatever you like!"
    ],
    
    # Jokes
    "tell me a joke": [
        "Why don’t skeletons fight each other? They don’t have the guts!",
        "What’s brown and sticky? A stick!",
        "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾"
    ],
    
    # Goodbye
    "bye": [
        "Goodbye! Come back soon!",
        "See you later, alligator! 🐊",
        "Bye! Stay awesome!"
    ],
    
    # Thanks
    "thank you": [
        "You're welcome! 😊",
        "Anytime!",
        "No problem at all!"
    ],
    
    # Default fallback
    "default": [
        "I’m still learning! Can you rephrase that?",
        "Interesting! Tell me more.",
        "I didn’t get that. Ask me something else!"
    ]
}

def chat(message, history):
    message = message.lower()
    for key in responses:
        if key in message:
            return random.choice(responses[key])
    return random.choice(responses["default"])

# Create interface
demo = gr.ChatInterface(
    fn=chat,
    title="🤖 Simple English Chatbot",
    examples=["Hi", "How are you?", "Tell me a joke", "Bye!"]
)

demo.launch()