import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_logs(logs):
    prompt = f"""
You are a DevOps expert.

Analyze this CI/CD failure log and provide:
1. Root cause
2. Fix suggestion (clear steps)

Logs:
{logs}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
