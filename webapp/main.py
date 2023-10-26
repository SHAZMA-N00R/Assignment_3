from transformers import pipeline
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

# Initialize the text generation and translation pipelines
generator = pipeline('text-generation', model='openai-gpt')
translator = pipeline('translation', model='Helsinki-NLP/opus-mt-en-de')

app = FastAPI()

class Body(BaseModel):
    text: str

@app.get('/')
def root():
    return HTMLResponse("<h1>A self-documenting API to interact with a GPT2 model and translate text</h1>")

@app.post('/generate')
def generate_text(body: Body):
    results = generator(body.text, max_length=35, num_return_sequences=1)
    return results[0]

@app.post('/translate')
def translate_text(body: Body):
    translation = translator(body.text)
    return translation[0]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
