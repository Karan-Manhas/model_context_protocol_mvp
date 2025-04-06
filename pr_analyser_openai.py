import os
import requests
import traceback
import json
import sys
import re
from dotenv import load_dotenv
from github_integration import fetch_pr_changes

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

def sanitize_filename(name: str) -> str:
    """Remove invalid characters for Windows/macOS file names."""
    return re.sub(r'[\\/*?:"<>|]', "", name)

class OpenAIPRAnalyzer:
    def fetch_pr(self, repo_owner: str, repo_name: str, pr_number: int):
        print(f" Fetching PR #{pr_number} from {repo_owner}/{repo_name}")
        try:
            pr_info = fetch_pr_changes(repo_owner, repo_name, pr_number)
            if pr_info is None:
                print(" No changes returned from fetch_pr_changes")
                return {}
            print(" Successfully fetched PR info")
            return pr_info
        except Exception as e:
            print(f" Error fetching PR: {str(e)}")
            traceback.print_exc()
            return {}

    def analyze_pr_with_openai(self, pr_data):

        # Comment out here Test Case for Trialling service (Bypasses OpenAI Client Request/Response)
        print(" Skip OpenAI analysis - mock analysis returned")
        return f"""
        PR Title: {pr_data['title']}
        Author: {pr_data['author']}
        Description: {pr_data['description']}

        Total Files Changed: {pr_data['total_changes']}
        Changed Files:
        {chr(10).join(f"- {f['filename']} ({f['status']})" for f in pr_data['changes'])}
        """
        # Comment out here Test Case for Trialling service (Bypasses OpenAI Client Request/Response)

        # Uncomment the following code to enable OpenAI analysis

        # print(" Sending PR data to OpenAI for analysis...")
        # try:
        #     simplified_pr = {
        #         'title': pr_data['title'],
        #         'description': pr_data['description'],
        #         'author': pr_data['author'],
        #         'total_changes': pr_data['total_changes'],
        #         'changes': [
        #             {
        #                 'filename': change['filename'],
        #                 'status': change['status'],
        #                 'additions': change['additions'],
        #                 'deletions': change['deletions'],
        #                 'patch': change.get('patch', '')[:1000]
        #             } for change in pr_data['changes']
        #         ]
        #     }

        #     headers = {
        #         'Content-Type': 'application/json',
        #         'Authorization': f'Bearer {OPENAI_API_KEY}'
        #     }

        #     data = {
        #         'model': 'gpt-3.5-turbo',
        #         'messages': [
        #             {
        #                 'role': 'system',
        #                 'content': 'You are a Software Engineer. Analyze the following pull request and provide a concise summary of the changes, their impact, and any potential issues.'
        #             },
        #             {
        #                 'role': 'user',
        #                 'content': json.dumps(simplified_pr)
        #             }
        #         ],
        #         'max_tokens': 1000
        #     }

        #     response = requests.post(
        #         'https://api.openai.com/v1/chat/completions',
        #         headers=headers,
        #         json=data
        #     )

        #     response.raise_for_status()
        #     result = response.json()
        #     analysis = result['choices'][0]['message']['content']
        #     return analysis

        # except Exception as e:
        #     error_msg = f" Error analyzing PR with OpenAI: {str(e)}"
        #     print(error_msg)
        #     traceback.print_exc()
        #     return error_msg

    def save_to_file(self, title: str, content: str):
        safe_title = sanitize_filename(title)
        file_name = f"{safe_title.replace(' ', '_')}.txt"
        try:
            with open(file_name, "w", encoding="utf-8") as f:
                f.write(f"{title}\n\n{content.strip()}")
            print(f" Saved analysis to file: {file_name}")
            return f"Saved to {file_name}"
        except Exception as e:
            error_msg = f" Error saving to file: {str(e)}"
            print(error_msg)
            traceback.print_exc()
            return error_msg

    def run_analysis(self, repo_owner, repo_name, pr_number):
        print(f" Starting analysis for PR #{pr_number}...")
        pr_data = self.fetch_pr(repo_owner, repo_name, pr_number)

        if not pr_data:
            print(" Failed to fetch PR data. Aborting.")
            return

        analysis = self.analyze_pr_with_openai(pr_data)

        page_title = f"PR Analysis: {pr_data['title']} (#{pr_number})"
        self.save_to_file(page_title, analysis)

        print(" Analysis complete!")
        return analysis

# Entry point
if __name__ == "__main__":
    analyzer = OpenAIPRAnalyzer()
    if len(sys.argv) > 3:
        repo_owner = sys.argv[1]
        repo_name = sys.argv[2]
        pr_number = int(sys.argv[3])
    else:
        repo_owner = 'repo_owner'
        repo_name = 'repo_name'
        pr_number = 2

    analysis = analyzer.run_analysis(repo_owner, repo_name, pr_number)
    print("\n Final Analysis Result:\n")
    print(analysis)
