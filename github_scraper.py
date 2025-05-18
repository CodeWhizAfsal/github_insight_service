import requests
from time import sleep



BASE_URL = "https://api.github.com"

import requests
import os

GITHUB_PAT = os.getenv("GITHUB_PAT")  # Set this in your .env or OS
HEADERS = {
    "Authorization": f"token {GITHUB_PAT}",
    "Accept": "application/vnd.github.v3+json"
}

def scrape_github_users(query):
    users = []
    for page in range(1, 3):  # Fetch first 2 pages
        search_url = f"https://api.github.com/search/users?q={query}&page={page}&per_page=10"
        response = requests.get(search_url, headers=HEADERS)
        if response.status_code != 200:
            print(f"[ERROR] GitHub Search API failed: {response.status_code}")
            continue

        data = response.json()
        for item in data.get("items", []):
            username = item["login"]
            user_url = f"https://api.github.com/users/{username}"
            user_response = requests.get(user_url, headers=HEADERS)

            if user_response.status_code != 200:
                print(f"[ERROR] Failed to fetch profile for {username}")
                continue

            user_data = user_response.json()
            user_profile = {
                "username": username,
                "profile_url": user_data.get("html_url"),
                "followers": user_data.get("followers"),
                "public_repos": user_data.get("public_repos"),
                "name": user_data.get("name"),
                "bio": user_data.get("bio"),
                "location": user_data.get("location"),
            }
            users.append(user_profile)

    return users


def fetch_user_profile(username):
    resp = requests.get(f"{BASE_URL}/users/{username}", headers=HEADERS)

    if resp.status_code != 200:
        print(f"[ERROR] Failed to fetch profile for {username}")
        return {}

    return resp.json()

if __name__ == "__main__":
    results = scrape_github_users("developer", pages=2)
    print(results)
