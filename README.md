Simple Customer Chatbot 🤖
This repository contains a simple, rule-based chatbot designed to handle basic customer inquiries. The chatbot uses a set of predefined patterns and responses to answer frequently asked questions, 
making it a great project for beginners to learn about natural language processing (NLP) fundamentals and chatbot development.

✨ Features
Rule-Based Responses: The chatbot matches user input to a dictionary of predefined patterns and provides a corresponding response.

Simple & Lightweight: No complex machine learning models are required, making it easy to understand and modify.

User-Friendly Interface: The chatbot runs in the command line, providing a simple way for users to interact with it.

🛠️ Installation
Clone the repository:

Bash

git clone https://github.com/gundu-ashritha20/simple-customer-chatbot.git
cd simple-customer-chatbot
Install dependencies:
This project has no external dependencies beyond Python's standard library.


🧠 How It Works
The core of the chatbot is a dictionary of patterns and responses. When a user enters a message, the chatbot:

Converts the input to lowercase for case-insensitive matching.

Checks the input against a list of known patterns (e.g., "hello", "how are you", "what is your return policy").

If a pattern matches, it returns a corresponding predefined response.

If no pattern matches, it provides a default "I don't understand" message.

This project can be easily extended by adding more patterns and responses to the rules dictionary in the chatbot.py file.


🤝 Contributing
Contributions are welcome! If you have ideas for new features or a better way to structure the code, feel free to open an issue or submit a pull request.



📜 License
This project is licensed under
