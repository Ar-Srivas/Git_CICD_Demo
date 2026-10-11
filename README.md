# MLOps Demo

## Overview
A simple Python-based machine learning demonstration that predicts a positive or negative label from an input value. The project demonstrates Git version control, automated testing, and CI using GitHub Actions. Uses hardcoded values since it is a Git experiment.

## Project Structure
- `app.py` — prediction function
- `test_app.py` — automated unit tests
- `requirements-dev.txt` — testing dependency
- `.github/workflows/python-ci.yml` — CI and artifact-upload workflow
- `data/` — sample dataset
- `.gitignore` — files excluded from version control

## Requirements
- Python 3.10 or later
- Git
- pytest

## Installation
```bash
python -m pip install -r requirements-dev.txt
```

## Run the Application
```bash
python app.py
```

## Run the Tests
```bash
python -m pytest -v
```

## CI/CD
GitHub Actions runs the automated tests when changes are pushed to `main` or a pull request targets `main`. If the tests pass, the workflow uploads the project files as an artifact that can be downloaded from the workflow run.
