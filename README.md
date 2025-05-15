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
git clone https://github.com/your-username/github-insight-service.git
cd github-insight-service
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
- **OpenAI API** – (Optional) for AI-based summarization  
- **Jinja2** – HTML templating engine for Flask  
- **JSON** – For internal data storage and caching  

---

## 🤔 Assumptions Made

- GitHub user data can be publicly scraped based on keyword search.
- The keyword query returns enough users to populate insights meaningfully.
- AI summarization is handled either via cohere.
- HTML template (`results.html`) expects a non-null results list.
- File `result.json` is used to cache or store intermediate results locally.

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
├── app.py                  # Main Flask app
├── ai_processor.py         # AI summarization logic
├── config.py               # Constants (e.g., API keys, base URLs)
├── github_scraper.py       # GitHub scraping logic
├── data.json               # Cached data file
├── requirements.txt
├── templates/
│   └── results.html        # Jinja2 HTML template
├── __pycache__/            # Compiled Python files
```

---

## 🪪 License

**MIT License** – See `LICENSE` for details.
