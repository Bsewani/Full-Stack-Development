import chainlit as cl
import requests

@cl.on_message
async def main(message: cl.Message):
    # This MUST be 8000 to match your working Backend
    api_url = "http://127.0.0.1:8000/ask"
    
    payload = {"question": message.content}
    
    try:
        # We wrap the request to prevent the 'Loop' error you saw earlier
        response = await cl.make_async(requests.post)(api_url, json=payload, timeout=30)
        
        if response.status_code == 200:
            answer = response.json().get("answer")
            await cl.Message(content=answer).send()
        else:
            await cl.Message(content="The Brain is awake but couldn't answer.").send()
    except Exception as e:
        await cl.Message(content="Cannot reach the Brain. Make sure Terminal 1 is running.").send()