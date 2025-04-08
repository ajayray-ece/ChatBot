import requests
import json
import os

# API key with sk-or-v1- format
api_key = "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"

class OpenAIBot:
    def __init__(self, engine):
        self.api_key = "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"
        self.api_url = "https://openrouter.ai/api/v1/chat/completions"
        self.engine = engine
        self.conversation_history = []

    def generate_response(self, prompt):
        try:
            # Add user message to history
            self.conversation_history.append({"role": "user", "content": prompt})
            
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://github.com/OpenRouterTeam/openrouter",
                "X-Title": "ChatBot"
            }
            
            messages = [
                {"role": "system", "content": "You are a helpful assistant."}
            ] + self.conversation_history
            
            data = {
                "model": "anthropic/claude-2",  # Using specific model
                "messages": messages,
                "temperature": 0.7,
                "max_tokens": 500
            }
            
            print("Sending request to API...")
            response = requests.post(
                self.api_url,
                headers=headers,
                json=data,
                timeout=30
            )
            
            print(f"Response status: {response.status_code}")
            
            if response.status_code == 200:
                result = response.json()
                if 'choices' in result and len(result['choices']) > 0:
                    bot_response = result['choices'][0]['message']['content'].strip()
                    # Add bot response to history
                    self.conversation_history.append({"role": "assistant", "content": bot_response})
                    return bot_response
                else:
                    print("No valid response in API result")
            
            print(f"API Response: {response.text}")
            return "I apologize, but I couldn't process your request at the moment."
            
        except Exception as e:
            print(f"Error during API call: {str(e)}")
            return "I apologize, but there was an error processing your request."