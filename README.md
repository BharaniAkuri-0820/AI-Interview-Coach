# AI Interview Coach

A beginner-friendly Flask web app for focused interview preparation. Choose a topic, take a timed quiz, review every answer, practice written interview responses, and track progress in SQLite.

## Features
- Home page and local candidate profile
- Python, Machine Learning, SQL, HR Interview, and Aptitude tests
- Ten multiple-choice questions per category with a 30-minute timer
- Automatic score calculation, confirmation, answer explanations, and performance levels
- Dashboard with attempts, average score, best score, and recommendations
- Interview practice with correctness, clarity, technical, and improvement feedback
- SQLite persistence through SQLAlchemy
- Deterministic feedback fallback when no AI key is configured

## Technology
Python, Flask, Flask-SQLAlchemy, SQLite, Jinja templates, HTML, CSS, JavaScript, and python-dotenv.

## Setup
1. Install Python 3.10 or newer and open this folder in VS Code.
2. Create and activate a virtual environment:
   - Windows PowerShell: `py -m venv .venv` then `.venv\\Scripts\\Activate.ps1`
   - macOS/Linux: `python3 -m venv .venv` then `source .venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and set a private `SECRET_KEY`. `OPENAI_API_KEY` is optional.
5. Run: `python main.py`
6. Open `http://127.0.0.1:5000`.

## Structure
- `app.py`: Flask configuration, database initialization, and application factory
- `main.py`: development entry point
- `models/`: SQLAlchemy models for users, attempts, and answers
- `routes/`: home, dashboard, quiz, and practice routes
- `data/questions.py`: category descriptions and question bank
- `services/`: feedback logic and future AI adapter boundary
- `templates/`: server-rendered pages
- `static/`: responsive CSS and quiz JavaScript

The SQLite file `interview_coach.db` is created automatically in the instance database location on first run. Never commit `.env` or real API keys.
