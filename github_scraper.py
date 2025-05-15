import requests
from time import sleep

HEADERS = {
    "Accept": "application/vnd.github+json",
    "User-Agent": "GitHub-Profile-Scraper",
}

BASE_URL = "https://api.github.com"

def scrape_github_users(query, pages=2, per_page=10, delay=2):
    users = []

    for page in range(1, pages + 1):
        print(f"[INFO] Fetching page {page} for query: '{query}'")

        params = {
            "q": query,
            "page": page,
            "per_page": per_page,
        }

        resp = requests.get(f"{BASE_URL}/search/users", headers=HEADERS, params=params)

        if resp.status_code != 200:
            print(f"[ERROR] API call failed: {resp.status_code} - {resp.text}")
            break

        data = resp.json()
        for item in data.get("items", []):
            username = item["login"]
            profile_url = item["html_url"]

            user_detail = fetch_user_profile(username)

            users.append({
                "username": username,
                "profile_url": profile_url,
                "name": user_detail.get("name"),
                "bio": user_detail.get("bio"),
                "location": user_detail.get("location"),
                "public_repos": user_detail.get("public_repos"),
                "followers": user_detail.get("followers"),
                "following": user_detail.get("following"),
                "extra": {
                    "pinned_repositories": []  # GitHub API doesn't expose pinned repos
                }
            })

        sleep(delay)
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
