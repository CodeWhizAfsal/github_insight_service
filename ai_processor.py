import cohere
from config import COHERE_API_KEY

client = cohere.Client(COHERE_API_KEY)

def get_insights(user):
    prompt = f"""
    Summarize this GitHub user's profile and infer their main skills, experience level, and technical expertise.

    Username: {user['username']}
    Name: {user.get('name', 'N/A')}
    Bio: {user.get('bio', 'N/A')}
    Location: {user.get('location', 'N/A')}
    Pinned Repositories: {', '.join(user['extra'].get('pinned_repositories', []))}
    """

    try:
        response = client.generate(
            model="command-r-plus",
            prompt=prompt,
            max_tokens=300,
            temperature=0.7
        )
        summary = response.generations[0].text.strip()
        user['insights'] = parse_summary(summary)
    except Exception as e:
        user['insights'] = {"error": str(e)}
    return user

def parse_summary(summary):
    return {"summary": summary}
