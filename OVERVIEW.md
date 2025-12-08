OVERVIEW

Goal: build an automated pipeline that runs tests & lint on PRs, deploys to staging on merge, and deploys to production via manual approval. Tech: Python (Django) backend, React frontend, Docker, GitHub Actions.


Repo Layout

/backend/
  app.py
  requirements.txt
  Dockerfile
  tests/
 /frontend/        (optional)
.github/workflows/
README.md
