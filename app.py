from flask import Flask, request, render_template, g
from github_scraper import scrape_github_users
from ai_processor import get_insights
from storage import store_data
from flasgger import Swagger
from datetime import datetime
import logging
import os

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

@app.before_request
def log_request():
    g.start_time = datetime.utcnow()
    logging.info(f"REQUEST - {request.method} {request.url} | BODY: {request.get_data(as_text=True)}")

@app.after_request
def log_response(response):
    duration = (datetime.utcnow() - g.start_time).total_seconds()
    logging.info(f"RESPONSE - {request.method} {request.url} | STATUS: {response.status_code} | TIME: {duration}s | BODY: {response.get_data(as_text=True)}")
    return response

# ----------------- GitHub Scrape Endpoint -----------------

@app.route('/scrape', methods=['GET'])
def scrape():
    """
    Scrape GitHub users based on a query.
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
    """
    query = request.args.get("q", "javascript developer")
    users = scrape_github_users(query)
    enriched_users = [get_insights(user) for user in users]
    store_data(users, enriched_users)
    return render_template("results.html", results=enriched_users)

# ----------------- Main Entry Point -----------------

if __name__ == '__main__':
    app.run(debug=True)
