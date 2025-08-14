# Tasks-Flask-Crud

# Tasks Flask CRUD

[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-3.x-black.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A minimal **Task Management API** built with **Flask**.  
It demonstrates clean CRUD endpoints, basic validation, and a simple in-memory store (great for learning).  
You can later swap the storage for SQLite or PostgreSQL.

---

## ✨ Features
- CRUD for tasks (`title`, `description`, `completed`)
- Proper HTTP status codes (`201` on create, `404` on not found)
- Clean JSON responses
- Simple, readable code structure (model + routes)
- Unit tests using Flask’s `test_client`

---

## 📦 Tech
- Python 3.10+
- Flask
- (Optional) Pytest for tests

---

## 📁 Project Structure
```text
Tasks-Flask-Crud/
├─ app.py                     # Flask app (routes/controllers)
├─ models/
│  └─ task.py                 # TaskManager model (to_dict)
├─ tests/
│  └─ test_app.py             # Unit tests with test_client
├─ requirements.txt
└─ README.md
