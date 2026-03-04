# FastAPI - Books Library

A simple FastAPI project to practice REST endpoints using an in-memory list of books.


---

## Features
- List all books
- Get a book by title
- Filter books by category (query param)
- Filter books by author (path param)

---

## Requirements
- Python 3.10+
- pip

---

## Project structure
```text
.
├── books.py
├── requirements.txt
└── README.md

---

## How to run

1. Create and activate a virtual environment:
	python3 -m venv .venv
	source .venv/bin/activate

---

2. Install dependencies:
	pip install -r requirements.txt

---

3. Start the server:
    uvicorn books:app --reload
	-Open	 
		- API: http://127.0.0.1:8000
		- Swagger UI: http://127.0.0.1:8000/docs

	-Endpoints (examples)

		-GET / → Welcome message

		-GET /books → List all books

		-GET /books/{book_title} → Get a book by title

		-GET /books/?category=science → Filter by category (query)

		-GET /books/author/{book_author} → Filter by author

	-Example
		-curl http://127.0.0.1:8000/books
