<h1 align="center"> IBM Full Stack Software Developer Certificate <br> Developing AI Applications with Python and Flask </h1>

## Emotion Detector

This is the final project within the course, "Developing AI Applications with Python and Flask" in the IBM Full Stack Software Developer Certificate. The objective of this project is to develop an AI-based Flask Web Application which will allow a user to provide a text string as input and receive a response from the AI which will tell the user what emotion is being conveyed in that text string.

More information about the course can be found [here](https://www.coursera.org/learn/python-project-for-ai-application-development/)



# Emotion Detection Web Application

## Project Overview

This project is an AI-based **Emotion Detection and Sentiment Analysis Web Application** built using **Watson NLP embedded libraries** and deployed with the **Flask framework**.

The application analyzes user-provided text and identifies the sentiment along with its confidence score. It has been modularized, tested, packaged, and deployed following software engineering best practices.

---

## Features

* AI-powered sentiment analysis using Watson NLP
* Extracts and formats relevant information from API responses
* Packaged as an importable Python module
* Unit tested for multiple input scenarios
* Flask-based web deployment
* Robust error handling (including HTTP 500 handling)
* PEP8-compliant code with static analysis validation

---

## Technologies Used

* Python 3.x
* Watson NLP Embedded Libraries
* Flask
* Requests
* Jinja2 (Flask templating)
* PEP8 (Code Quality Standards)

---

## Project Structure

```
EmotionDetector/
│
├── server.py
├── SentimentAnalysis/
│   └── sentiment_analysis.py
│
├── templates/
│   └── index.html
│
└── tests/
```

---

## Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone <your-repository-url>
cd practice_project
```

### 2️⃣ Install Dependencies

```bash
pip install flask requests
```

### 3️⃣ Run the Application

```bash
python server.py
```

The application will be available at:

```
http://localhost:5000
```

---

## Running Unit Tests

Unit tests were implemented to validate:

* Correct sentiment detection
* Proper formatting of output
* Handling of empty or invalid input
* Error response validation

To run tests:

```bash
python -m unittest
```

---

## 🔍 How It Works

1. User inputs text via the web interface.
2. Flask receives the request.
3. The `sentiment_analyzer()` function sends the text to the Watson NLP API.
4. The API returns structured JSON.
5. Relevant fields (`label`, `score`) are extracted.
6. A formatted response is displayed to the user.
7. If an error occurs (e.g., invalid input or API issue), appropriate error handling ensures the application does not crash.

---

## Error Handling

The application handles:

* Missing input text
* External API failures
* Invalid JSON structures
* HTTP 500 server errors

This prevents unexpected crashes and ensures a stable user experience.

---

