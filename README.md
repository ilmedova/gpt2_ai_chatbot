This is a simple chatbot using GPT2 model, PyTorch and Transformers.
To test the API you can send POST request to http://127.0.0.1:5000/chat with content: {"user_input": "Replace me by any text you'd like."}
Or you can simply send request using curl:

```shell
curl -X POST http://127.0.0.1:5000/chat -H "Content-Type: application/json" -d '{"user_input": "Replace me by any text you would like"}'
```
