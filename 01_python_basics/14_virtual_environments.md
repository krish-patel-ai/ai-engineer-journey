# Day 14 — Virtual Environments & pip

## Commands Practiced
- python -m venv venv
- source venv/bin/activate
- pip install numpy pandas requests
- pip freeze > requirements.txt
- deactivate

## Key Learnings
- Every project needs its own virtual environment
- requirements.txt lets anyone recreate your environment
- Never push venv/ folder to GitHub
- pip freeze captures exact package versions