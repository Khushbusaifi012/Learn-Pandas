import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Step 1: Set model name and your HF token
model_name = "microsoft/DialoGPT-medium"
HF_TOKEN = "hf_LyCdYWlaDXOUanOmIJmXLblgHoJuEeJLn"  #huggingfaceapitoken

# Step 2: Load model and tokenizer using token
model = AutoModelForCausalLM.from_pretrained(model_name, use_auth_token=HF_TOKEN)
tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=HF_TOKEN)

# Step 3: Chatbot function
def chatbot():
    print("Hello! I'm your chatbot. Type 'exit' to end the conversation.")

    # Initialize the conversation history
    chat_history_ids = None

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Encode the input and add it to the conversation history
        new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
        
        # Limit conversation history to a maximum length (e.g., last 1000 tokens)
        if chat_history_ids is None:
            chat_history_ids = new_input_ids
        else:
            chat_history_ids = torch.cat([chat_history_ids, new_input_ids], dim=-1)
        
        # Keep the conversation history to a reasonable size
        max_history_length = 1000  # Adjust this as needed
        if chat_history_ids.shape[-1] > max_history_length:
            chat_history_ids = chat_history_ids[:, -max_history_length:]

        # Generate response with some randomness for more variety
        bot_output = model.generate(chat_history_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id, top_k=50, top_p=0.95, temperature=0.7)
        
        # Get the response and decode
        response = tokenizer.decode(bot_output[:, chat_history_ids.shape[-1]:][0], skip_special_tokens=True)

        print(f"Bot: {response}")

# Step 4: Run it
chatbot()
