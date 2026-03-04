PT - BR
# FastAPI - Library (Books)

Projeto simples em FastAPI para treinar rotas (GET) usando uma lista em memória.

## Requisitos
- Python 3.10+ (recomendado)
- pip

## Como rodar

### 1) Criar e ativar o ambiente virtual
```bash
python3 -m venv .venv
source .venv/bin/activate

### 2) Instalar dependências
pip install -r requirements.txt

### 3) Rodar o servidor
uvicorn books:app --reload
#Acesse
API: http://127.0.0.1:8000
Docs Swagger: http://127.0.0.1:8000/docs


EN

# FastAPI - Library (Books)

A simple FastAPI project to practice routes (GET) using an in-memory list of books.

## Requirements
- Python 3.10+ (recommended)
- pip

## How to run

### 1) Create and activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate

### 2) Install Dependencies
pip install fastapi uvicorn

### 3) Start the server
uvicorn books:app --reload

#Open:
API: http://127.0.0.1:8000
Swagger Docs: http://127.0.0.1:8000/docs
