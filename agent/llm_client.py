import os
import google.generativeai as genai

# Configure API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


models = genai.list_models()

for m in models:
    print(m.name, m.supported_generation_methods)


# Create model
model = genai.GenerativeModel("gemini-pro-latest")

def analyze_logs(logs):
    prompt = f"""
You are a DevOps expert.

Analyze this CI/CD failure log and provide:
1. Root cause
2. Fix suggestion (step-by-step)

Logs:
{logs}
"""

    response = model.generate_content(prompt)
    return response.text


# Example usage
if __name__ == "__main__":
    logs = "Error: Docker build failed due to missing file package.json"

    result = analyze_logs(logs)
    print(result)
