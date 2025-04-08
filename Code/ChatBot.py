# Importing Bot Definition
import sys
import os

# Add the Code directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

from BotDefinition import OpenAIBot

def main():
    # Using OpenRouter's Claude model
    engine = "anthropic/claude-2"
    print("Using OpenRouter AI Chat Model")
    print("-----------------------------")
    
    try:
        chatbot = OpenAIBot(engine)
        print("Chat initialized! Type 'END CHAT' to exit.")
        print("You can start chatting now...")
        
        while True:
            # Get Prompt from User
            prompt = input("\nYou: ").strip()

            # User can stop the chat by sending 'End Chat' as a Prompt
            if prompt.upper() == 'END CHAT':
                print("\nGoodbye! Chat session ended.")
                break

            if not prompt:
                print("Please enter a message!")
                continue

            # Generate and Print the Response from ChatBot
            print("\nBot: ", end="")
            response = chatbot.generate_response(prompt)
            if response:
                print(response)

    except KeyboardInterrupt:
        print("\nChat session interrupted. Goodbye!")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")

if __name__ == "__main__":
    main()