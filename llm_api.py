from fastapi import FastAPI, Request
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch, os
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("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")
MODEL_ID = os.getenv("RapidS0C/V2-seneca-x-deepseek-r1-distill-qwen-32b-v1.3-safe")

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, use_auth_token=HF_TOKEN)

print("Loading model...")
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.float16,
    device_map="auto",
    use_auth_token=HF_TOKEN
)

app = FastAPI()

@app.post("/ask")
async def ask(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs, max_new_tokens=900)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"response": response}
