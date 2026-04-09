import requests
import os

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

def get_logs(repo, run_id):
    url = f"https://api.github.com/repos/{repo}/actions/runs/{run_id}/logs"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        return response.text[:5000]  # truncate logs
    else:
        return "Failed to fetch logs"

def comment_on_pr(repo, issue_number, comment):
    url = f"https://api.github.com/repos/{repo}/issues/{issue_number}/comments"
    
    requests.post(url, headers=HEADERS, json={
        "body": f"🤖 AI Agent Analysis:\n\n{comment}"
    })
