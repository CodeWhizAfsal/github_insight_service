from flask import Flask, request, render_template
from github_scraper import scrape_github_users
from ai_processor import get_insights
from storage import store_data

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def scrape():
    query = request.args.get("q", "javascript developer")
    users = scrape_github_users(query)
    enriched_users = [get_insights(user) for user in users]
    store_data(users, enriched_users)
    return render_template("results.html", results=enriched_users)

if __name__ == '__main__':
    app.run(debug=True)
