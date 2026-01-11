from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a chatbot instance
chatbot = ChatBot('VirtualAssistant')

# Create a trainer
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on English corpus
trainer.train('chatterbot.corpus.english')

# Greet the user
print("Hello! I am your virtual assistant. How can I help you today?")

# Main loop for conversation
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("Assistant: Goodbye!")
        break
    print(f"You said: {user_input}")
    response = chatbot.get_response(user_input)
    print(f"Assistant: {response}")
