# Catalog AI

Backend system for product catalog normalization and deduplication.

This project simulates a real-world backend system that processes messy supplier product catalogs and prepares them for further normalization and matching.

The goal is to eventually build an AI-assisted system that can detect duplicate products coming from different suppliers.

---

## Learning Purpose

This project is being developed as a **learning and portfolio project** while studying:

- backend development with FastAPI
- database design with SQLAlchemy
- REST API architecture
- product catalog data processing
- AI-assisted catalog matching (planned)

The project is being built step-by-step while learning new backend concepts.

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

All of these refer to the **same product**, but appear as different entries in a catalog.

The goal of this project is to build tools that help normalize and match such products automatically.

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

## Current Features

- FastAPI backend
- Supplier API
- SQLite database
- SQLAlchemy ORM
- CRUD operations for suppliers

Endpoints:

GET /suppliers  
POST /suppliers

---

## Running the Project

Clone the repository:


git clone https://github.com/YOUR\_USERNAME/catalog-ai.git


Go to backend folder:


cd catalog-ai/backend


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

## Planned Features

Future steps for the project:

- product feed ingestion
- product catalog normalization
- product attribute extraction
- duplicate detection
- embedding-based product matching
- AI-assisted catalog processing