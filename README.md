<h1 align="center">Youtube Fetch API</h1>

## About

Fampay Assignment

## Installation

    python3 -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt
    cd yt_video_fetcher
    python3 manage.py migrate

## Runnning the server

    python3 manage.py runserver

### Project Aim

To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

## API Documentation:

---

A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.

    Endpoint 	: /videos
