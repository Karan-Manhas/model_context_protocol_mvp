import os
import requests
import traceback
from dotenv import load_dotenv

load_dotenv()
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

def fetch_pr_changes(repo_owner: str, repo_name: str, pr_number: int) -> list:
    """Fetch changes from a GitHub pull request.
    
    Args:
        repo_owner: The owner of the GitHub repository
        repo_name: The name of the GitHub repository
        pr_number: The number of the pull request to analyze
        
    Returns:
        A list of file changes with detailed information about each change
    """
    print(f" Fetching PR changes for {repo_owner}/{repo_name}#{pr_number}")
    
    pr_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls/{pr_number}"
    files_url = f"{pr_url}/files"
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    
    try:
        pr_response = requests.get(pr_url, headers=headers)
        pr_response.raise_for_status()
        pr_data = pr_response.json()
        
        files_response = requests.get(files_url, headers=headers)
        files_response.raise_for_status()
        files_data = files_response.json()
        
        changes = []
        for file in files_data:
            change = {
                'filename': file['filename'],
                'status': file['status'],  # added, modified, removed
                'additions': file['additions'],
                'deletions': file['deletions'],
                'changes': file['changes'],
                'patch': file.get('patch', ''),  # The actual diff
                'raw_url': file.get('raw_url', ''),
                'contents_url': file.get('contents_url', '')
            }
            changes.append(change)
        
        pr_info = {
            'title': pr_data['title'],
            'description': pr_data['body'],
            'author': pr_data['user']['login'],
            'created_at': pr_data['created_at'],
            'updated_at': pr_data['updated_at'],
            'state': pr_data['state'],
            'total_changes': len(changes),
            'changes': changes
        }
        
        print(f"Successfully fetched {len(changes)} changes")
        return pr_info
        
    except Exception as e:
        print(f"Error fetching PR changes: {str(e)}")
        traceback.print_exc()
        return None

pr_data = fetch_pr_changes('USERNAME', 'REPO_NAME', 2)
print(pr_data) 