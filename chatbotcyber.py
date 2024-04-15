#!/usr/bin/env python3
import nltk
from nltk.chat.util import Chat, reflections
import langid
import speech_recognition as sr
import pyttsx3
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os
import time


# Download the NLTK data (if not already downloaded)
nltk.download('vader_lexicon')

# Create a sentiment analyzer
sentiment_analyzer = SentimentIntensityAnalyzer()

# Create a sentiment analyzer
sentiment_analyzer = SentimentIntensityAnalyzer()



# Define patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you', ['I am doing well, thank you!', 'I am a chatbot, so I don\'t have feelings, but thanks for asking!']),
    (r'what is your name', ['I am a chatbot created with NLTK.', 'You can call me Chatbot.']),
    (r'weather', ['I am not connected to the internet, so I cannot provide real-time weather information.']),
    (r'bye|goodbye', ['Goodbye!', 'Bye! Have a great day.']),
    (r'(.*)', ["'I'm sorry, I don\'t understand.'"]),
]

# Knowledge Base dictionary
knowledge_base = {
    'python': 'Python is a versatile programming language often used for web development, data analysis, and artificial intelligence.',
    'nlp': 'Natural Language Processing (NLP) is a field of study focusing on the interaction between computers and human languages.',
    'chatbot': 'A chatbot is a computer program designed to simulate conversation with human users, providing information or assistance.',
    'machine learning': 'Machine learning is a subset of artificial intelligence that enables computers to learn from data and make predictions or decisions.',
    'data science': 'Data science is a multidisciplinary field that uses scientific methods, processes, algorithms, and systems to extract insights from structured and unstructured data.',
    'algorithm': 'An algorithm is a step-by-step procedure or formula for solving problems or accomplishing tasks.',
    'neural network': 'A neural network is a set of algorithms modeled after the human brain, designed to recognize patterns.',
    'programming': 'Programming is the process of designing and building an executable computer program for accomplishing a specific task.',
    'web development': 'Web development involves building and maintaining websites and web applications.',
    'cloud computing': 'Cloud computing is the delivery of computing services, including servers, storage, databases, networking, analytics, and intelligence, over the internet to offer faster innovation and flexible resources.',
}

# Predefined user credentials
valid_username = "user123"
valid_password = "pass123"

# Create a chatbot
chatbot = Chat(patterns, reflections)

# Text-to-speech engine setup
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    print(f"ChatBot: {text}")
    engine.say(text)
    engine.runAndWait()

# Function for automatic model retraining
def automatic_retrain(knowledge_base, chatbot):
    while True:
        time.sleep(5)  # Check for modifications every 5 seconds
        new_knowledge_base = {
            'new_topic': 'This is a new topic added dynamically during runtime.',
            # Add more entries as needed
        }
        knowledge_base.update(new_knowledge_base)

        # Update the chatbot patterns
        chatbot._pairs.extend([(rf'{key}', value) for key, value in new_knowledge_base.items()])

        print("Retraining complete.")

# Function for interactive learning
def interactive_learning(user_input, chatbot, knowledge_base):
    corrected_response = input(f"I didn't understand. Can you provide a suitable response for '{user_input}'? ")
    knowledge_base[user_input.lower()] = corrected_response
    print("Thank you for teaching me!")

# User authentication
speak("Welcome to the Chatbot!")
print("Welcome to the Chatbot!")
while True:
    speak("Enter username")
    print("Response: ", end="")
    username = input()
    speak("Enter password")
    print("Response: ", end="")
    password = input()

    if username == valid_username and password == valid_password:
        print("Authentication successful! You can now chat with the bot.")
        speak("Authentication successful! You can now chat with the bot.")
        break
    else:
        print("Invalid credentials. Please try again.")
        speak("Invalid credentials. Please try again.")

# Run the chatbot
print("Hello! I'm your chatbot. Type 'bye' to exit.")
while True:
    print('Response: ', end="")
    user_input = input()

    if user_input.lower() == 'bye':
        print('Goodbye!')
        break

    # Detect the language of the user's input
    lang, _ = langid.classify(user_input)

    # Use language information to customize responses
    if lang == 'en':
        # Analyze sentiment
        sentiment_score = sentiment_analyzer.polarity_scores(user_input)

        if sentiment_score['compound'] >= 0.05:
            print("User Input has a positive sentiment!")
            speak("User Input has a positive sentiment!")
        elif sentiment_score['compound'] <= -0.05:
            print("User Input has a negative sentiment!")
            speak("User Input has a negative sentiment!")
        else:
            print("User Input has a neutral sentiment.")
            speak("User Input has a neutral sentiment.")

        if user_input.lower() in knowledge_base:
            response = knowledge_base[user_input.lower()]
        else:
            response = chatbot.respond(user_input)
            speak(response)
            correct_response = input("Was the response correct? (yes/no): ")
            if correct_response.lower() == 'no':
                interactive_learning(user_input, chatbot, knowledge_base)
    elif lang == 'es':
        speak("Lo siento, actualmente solo hablo inglés.")
    else:
        speak("I'm sorry, I don't understand other languages at the moment.")
