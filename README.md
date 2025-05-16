# 🔍 GitHub Insight Service

A Flask-based web application that scrapes GitHub profiles based on a search query and summarizes developer insights using Cohere's language model API.

---

## 🔧 Tech Stack

- **Backend**: Python, Flask  
- **Web Scraping**: GitHub Search + Requests  
- **AI Summarization**: Cohere API  
- **Frontend**: HTML (Jinja2 Templates)  
- **Data Handling**: JSON  
- **Storage**: Local filesystem (`data.json`)  

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://https://github.com/CodeWhizAfsal/github_insight_service
cd github_insight_service
```
### 2. Create Virtual Environment
```bash
python3 -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

**Example `requirements.txt`:**
```text
flask
requests
beautifulsoup4
openai  # Optional for AI summaries
```

---

## 🧰 Tech Stack Used

- **Python 3.12**
- **Flask** – Web application framework  
- **BeautifulSoup** – Web scraping GitHub profiles  
- **Requests** – HTTP requests to GitHub  
- **Cohere** –  for AI-based summarization  
- **Jinja2** – HTML templating engine for Flask  
- **JSON** – For internal data storage and caching  

---

## 🤔 Assumptions Made

- GitHub user data can be publicly scraped based on keyword search.
- The keyword query returns enough users to populate insights meaningfully.
- AI summarization is handled either via cohere.
- HTML template (`results.html`) expects a non-null results list.
- File `data.json` is used to cache or store intermediate results locally.

---

## 🚀 Running Locally

### Start Flask App
```bash
python app.py
```

By default, this runs at:

[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

### Using the Web UI

1. Navigate to `/` in your url.
2. Enter a keyword (e.g., `"machine learning"`) to fetch.

---

## 📡 API Endpoints

### `GET /`
**Description:** Displays a form to input keyword and number of users.  
**Returns:** HTML page (Jinja template)

---

### `POST /results`

**Description:** Accepts keyword and count, scrapes GitHub users, processes them via AI, and renders results.  
**Payload:**
```json
{
  "query": "python",
  "count": 5
}
```
**Returns:** Rendered `results.html` with summaries.

---

### `GET /api/results` (Optional REST endpoint)

**Returns:**
```json
{
  "users": [
    {
      "username": "octocat",
      "summary": "This user specializes in Python backend services and open-source contributions."
    }
  ]
}
```

---

## 📂 Project Structure

```bash
github_insight_service/
├──README.md                       # Project overview
├── app.py                           # Main Flask app with logging & routes
├── requirements.txt                 # Python dependencies
├── Dockerfile                       # Docker build file for the Flask app
├── docker-compose.yml              # Compose file to run app + optional DB
├── logs/
│   └── app.log                      # Request/response logs (auto-created)
├── github_scraper.py               # Your GitHub scraping logic
├── ai_processor.py                 # AI/LLM-based summarization
├── storage.py                      # Data storage logic (DB or JSON)
├── templates/
│   └── results.html                # Renders enriched GitHub user insights
└── swagger/
    └── swagger.yaml                # Swagger/OpenAPI spec file

```

---

## 🪪 License

**MIT License** – See `LICENSE` for details.
