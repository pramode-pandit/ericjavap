import os
from github_client import get_logs, comment_on_pr
from llm_client import analyze_logs

repo = os.getenv("REPO")
run_id = os.getenv("RUN_ID")

def main():
    print("Fetching logs...")
    logs = get_logs(repo, run_id)

    print("Analyzing with AI...")
    analysis = analyze_logs(logs)

    print("Analysis:\n", analysis)

    # OPTIONAL: Hardcode PR for now OR fetch dynamically
    pr_number = 1  

    print("Posting comment...")
    comment_on_pr(repo, pr_number, analysis)

if __name__ == "__main__":
    main()
