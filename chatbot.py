import re
import random

def get_response(user_input):
    """
    Determines the chatbot's response based on a user's input.
    Uses regular expressions to match patterns.
    """
    
    # Define patterns and corresponding responses
    patterns = [
        # Greeting patterns
        (re.compile(r'\b(hello|hi|hey)\b', re.IGNORECASE),
         ['Hello! How can I assist you today? 😃', 'Hi there! What can I help you with?']),

        # Order status queries
        (re.compile(r'\b(my order|order status|where is my order)\b', re.IGNORECASE),
         ['I can help with that. Please provide your order number.', 'To check your order status, please provide your order ID.']),

        # Shipping information queries
        (re.compile(r'\b(shipping|delivery|shipment)\b', re.IGNORECASE),
         ['Standard shipping takes 3-5 business days.', 'Shipping costs vary based on location.']),

        # Return policy queries
        (re.compile(r'\b(return|refund|exchange|policy)\b', re.IGNORECASE),
         ['Our return policy allows for returns within 30 days of purchase.', 'You can start a return online or contact our support team.']),

        # Thank you responses
        (re.compile(r'\b(thank you|thanks)\b', re.IGNORECASE),
         ['You\'re welcome!', 'Glad I could help!', 'Is there anything else I can assist you with?']),

        # Default fallback response for unmatched queries
        (re.compile(r'.*'),
         ["I'm sorry, I don't understand that. Can you please rephrase?",
          "I'm not sure how to respond to that.",
          "Can you be more specific?"])
    ]

    user_input = user_input.lower().strip()

    # Iterate through patterns to find a match
    for pattern, responses in patterns:
        if re.search(pattern, user_input):
            return random.choice(responses)
    
    # This line is a final fallback if the loop completes without a match, though the last regex should catch everything
    return "I'm not sure how to respond to that."

def start_chatbot():
    """
    Main function to run the chatbot loop.
    """
    print("👋 Hello! I'm your customer service chatbot. Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Chatbot: Goodbye! Have a great day! 👋")
            break
        
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    start_chatbot()