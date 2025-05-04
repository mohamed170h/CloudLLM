# RunPod Deployment Guide for Seneca-X LLM API (64GB Model)

## Purpose
This guide explains how to deploy the 64GB `seneca-x-deepseek-r1-distill-qwen-32b-v1.3-safe` model on RunPod using a single A100 GPU. It includes authentication setup and FastAPI-based LLM serving.

---

## 🧱 Requirements
- RunPod account: https://runpod.io
- Hugging Face account (with model uploaded)
- Your Hugging Face token (HF_TOKEN)
- A100 80GB GPU (preferred) or A100 40GB with CPU offloading

---

## ✅ 1. Deploy RunPod GPU Pod
1. Go to your RunPod dashboard.
2. Click “Deploy a Pod”
3. Choose:
   - Template: `Custom Image`
   - Docker Image: `python:3.10-slim`
   - GPU: Select **A100 80GB** or **A100 40GB**
   - Expose port: **8000**
   - Disk size: **100 GB** (minimum)
4. Click **Deploy Pod**

---

## ✅ 2. Upload Code
1. Upload `cloud-llm-deployment.zip` via the “Connect” > “File Upload” menu.
2. Inside terminal:
```bash
unzip cloud-llm-deployment.zip
cd cloud-llm
nano .env  # Edit the environment variables:
```

Sample `.env`:
```
HF_TOKEN=hf_xxx...
MODEL_ID=your-hf-username/your-model-name
API_SECRET=yourcustomsecretkey123
```

---

## ✅ 3. Install Dependencies
```bash
apt update && apt install -y git gcc g++ libssl-dev
pip install --upgrade pip
pip install -r requirements.txt
```

---

## ✅ 4. Run the Server
```bash
uvicorn llm_api:app --host 0.0.0.0 --port 8000
```

This will start the LLM server and expose it on public port 8000.

---

## ✅ 5. Query the Model
Make a POST request from your local backend (RAG/SIEM/SOAR):

```python
import requests

headers = {"Authorization": "Bearer yourcustomsecretkey123"}
response = requests.post("http://<runpod-public-ip>:8000/ask", 
                         headers=headers, 
                         json={"prompt": "Describe this IOC..."})
print(response.json())
```

---

## ✅ Notes
- Shut down the pod when not in use to save cost.
- Add rate limiting or HTTPS reverse proxy if needed.
- A100 40GB may require offloading to CPU (`device_map="auto"`).

---