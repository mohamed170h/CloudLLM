RunPod LLM API Deployment

1. Upload this folder to your RunPod container.
2. Inside terminal:
   $ unzip cloud-llm-deployment.zip
   $ cd cloud-llm
   $ nano .env    # replace tokens
3. Install dependencies:
   $ pip install --upgrade pip
   $ pip install -r requirements.txt
4. Run the server:
   $ python3 llm_api.py or ./start.sh

Call your model with:
POST http://<public_runpod_url>:8000/ask
Headers: Authorization: Bearer <your_API_SECRET>
Body: { "prompt": "your input here" }