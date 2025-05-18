from flask import Flask, request, jsonify, g
from github_scraper import scrape_github_users
from ai_processor import get_insights
from storage import store_data
from flasgger import Swagger
from datetime import datetime
import logging
import os
from datetime import datetime, timezone

# Create logs directory if not exists
os.makedirs('logs', exist_ok=True)

# Configure logging
logging.basicConfig(
    filename='logs/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

app = Flask(__name__)
swagger = Swagger(app, template_file='swagger/swagger.yaml')

# ---------- Request/Response Logging Middleware ----------

from datetime import datetime, timezone

@app.before_request
def before_request():
    g.start_time = datetime.now(timezone.utc)


@app.after_request
def log_response(response):
    end_time = datetime.now(timezone.utc)
    duration = (end_time - g.start_time).total_seconds()
    
    if response.direct_passthrough:
        body = "[direct passthrough — not logged]"
    else:
        body = response.get_data(as_text=True)

    logging.info(
        f"RESPONSE - {request.method} {request.url} | "
        f"STATUS: {response.status_code} | TIME: {duration:.3f}s | BODY: {body}"
    )
    return response



# ----------------- JSON API Endpoint Only -----------------

@app.route('/api/scrape', methods=['GET'])
def scrape_api():
    """
    Scrape GitHub users and return structured summaries via JSON.
    ---
    parameters:
      - name: q
        in: query
        type: string
        required: false
        default: "javascript developer"
    responses:
      200:
        description: A list of enriched GitHub users
        examples:
          application/json: {
            "results": [
              {
                "username": "octocat",
                "profile_url": "https://github.com/octocat",
                "followers": 100,
                "public_repos": 50,
                "insights": "An active contributor..."
              }
            ]
          }
    """
    query = request.args.get("q", "javascript developer")
    users = scrape_github_users(query)
    enriched_users = [get_insights(user) for user in users]
    store_data(users, enriched_users)
    return jsonify({"results": enriched_users})

# ----------------- Main Entry Point -----------------

if __name__ == '__main__':
    app.run(debug=True)
