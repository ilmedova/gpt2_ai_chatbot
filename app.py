from flask import Flask, request, jsonify
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

app = Flask(__name__)

# Load pre-trained model and tokenizer
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Set up model to generate responses
model.eval()

# Define chat endpoint
@app.route("/chat", methods=["POST"])
def chat():
    # Get user input from request
    user_input = request.json["user_input"]

    # Tokenize user input
    input_ids = tokenizer.encode(user_input, return_tensors="pt")

    # Generate response
    with torch.no_grad():
        output_ids = model.generate(input_ids, max_length=100, num_return_sequences=1)

    # Decode and format response
    response = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
