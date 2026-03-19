# Catalog AI

Backend system for product catalog normalization and deduplication.

This project simulates a real-world backend system that processes inconsistent supplier product data and prepares it for normalization and matching.

The long-term goal is to build an AI-assisted system capable of detecting duplicate products across multiple suppliers.

---

## Project Purpose

This is a **learning + portfolio project** focused on backend development and real-world data problems.

The project is built step-by-step while learning:

- FastAPI (REST API development)
- SQLAlchemy (ORM and database interaction)
- database design
- data normalization workflows
- AI-assisted product matching (planned)

---

## Problem

Supplier product catalogs are often inconsistent.

Example:

Supplier A  
Nike Air Max 90 Black 42  

Supplier B  
Nike AirMax 90 Men's Black Size 42  

Supplier C  
Air Max 90 Nike Black EU42  

All of these refer to the same product, but appear as separate entries.

This project aims to build a system that can:

- standardize product data
- extract attributes
- detect duplicates across suppliers

---

## Tech Stack

Backend:

- Python
- FastAPI
- SQLAlchemy
- SQLite

Tools:

- Git
- GitHub
- Uvicorn

---

## Architecture Direction

The project is being developed backend-first, with a planned transition into a full-stack application.

Planned frontend:

- React
- TypeScript

The frontend will be used for:

- managing supplier data
- visualizing normalized products
- reviewing duplicate matches

## Current Features

- FastAPI backend
- SQLite database
- SQLAlchemy ORM
- Supplier entity
- Full CRUD API for suppliers
- Request validation with Pydantic

---

## API Endpoints

Suppliers:

- GET /suppliers → get all suppliers  
- GET /suppliers/{id} → get supplier by id  
- POST /suppliers → create supplier  
- PUT /suppliers/{id} → update supplier  
- DELETE /suppliers/{id} → delete supplier  

---

## Running the Project

Clone the repository:


git clone https://github.com/PerSei01/AI-powered-catalog-normalization.git


Go to backend folder:


cd backend


Create virtual environment:


python -m venv .venv


Activate environment (Windows):


.venv\Scripts\activate


Install dependencies:


pip install fastapi uvicorn sqlalchemy


Run server:


uvicorn main:app --reload


Open API docs:


http://127.0.0.1:8000/docs


---

## Project Structure (current)


backend/
├── main.py
├── database.py
├── models.py
└── ...


(Structure will be expanded as the project grows)

---

## Planned Features

Next steps:

- product entity and catalog ingestion
- product normalization logic
- attribute extraction (brand, model, size, etc.)
- duplicate detection
- embeddings for product similarity
- AI-assisted matching system

---

## Notes

This project is being developed incrementally with focus on:

- understanding backend fundamentals
- building production-like structure
- writing clean and predictable API logic