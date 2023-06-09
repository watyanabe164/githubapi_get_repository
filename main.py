# github apiを使用して、指定URLのリポジトリを取得する
import os
import requests

owner = "watyanabe164"
repo = "sh00072021_dev"
url = f"https://api.github.com/repos/{owner}/{repo}/contents/README.md"
token = "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"
output_file = "binary_file.md"

print(url)  

headers = {
    "Authorization": f"Token {token}",
    "Accept": "application/vnd.github.v3+json"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    content = response.json()
    file_content = requests.get(content['download_url']).content
    with open(output_file, "wb") as f:
        f.write(file_content)
    print(f"File saved to {os.path.abspath(output_file)}")
else:
    print(f"Failed to retrieve file. Status code: {response.status_code}")