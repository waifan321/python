import pandas as pd 
import re 

def chat():
    print("hello! how can I help you today?")
    while True:
        user_message = input("You: ")
        if re.search(r'quit', user_message, re.IGNORECASE):
            print("Goodbye!")
            break

        user_response = user_message.lower()
        if user_response in responses:
            print("Bot: " + responses[user_response])
        else:
            print("Bot: I'm sorry, I do not understand. Please try again.")

# Load the intents JSON file
json_obj = pd.read_json("json/intents.json")

# Extract responses from the JSON object
responses = {}
for intent in json_obj['intents']:
    for pattern in intent['patterns']:
        responses[pattern.lower()] = intent['responses'][0]

# Start the chat
chat()
