# 📝 Flask Blog (JSON-Based CRUD App)

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-black)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-success)
![Bootcamp](https://img.shields.io/badge/Masterschool-Bootcamp-orange)
![Platform](https://img.shields.io/badge/Platform-Web-lightgrey)

> A simple **Flask blog application** built with **Python + JSON file storage**.  
> This project demonstrates CRUD operations without a database.

---

# 📌 Overview

This project demonstrates how to:

- Build a web app using Flask
- Handle GET and POST requests
- Use JSON as a simple data storage
- Implement full CRUD functionality
- Create and process HTML forms
- Structure a small web application
- Refactor repeated logic into helper functions

---

# 🖥️ Demo Flow

1. User opens the homepage  
2. All blog posts are displayed  
3. User can:
   - Add a new post
   - Update an existing post
   - Delete a post  

Example:

```bash
python app.py
```

Open in browser:

http://127.0.0.1:5000

---

# ✨ Core Features

- Display all blog posts
- Add new posts via form
- Update existing posts
- Delete posts
- Persistent storage using JSON file
- Clean UI with CSS styling
- Refactored file handling (load/save functions)

---

# 📂 Project Structure

flask-blog/
│
├── app.py
├── data/
│   └── posts.json
├── templates/
│   ├── index.html
│   ├── add.html
│   └── update.html
├── static/
│   └── style.css
├── requirements.txt
└── README.md

---

# 🚀 Installation & Usage

## Requirements

- Python 3.10+

Install dependencies:

pip install -r requirements.txt

---

## Run the App

python app.py

---

# 🧠 Technical Concepts Applied

- Flask routing
- GET vs POST requests
- HTML forms handling
- JSON file handling
- CRUD operations
- Jinja2 templating
- Refactoring with helper functions
- Basic error handling

---

# 🔐 Error Handling

The application handles:

- Missing JSON file
- Invalid JSON format
- File write errors
- Missing blog post (404)

---

# 🎓 Learning Objectives

- Understand Flask fundamentals
- Build full CRUD applications
- Work with JSON as storage
- Handle form data
- Improve code structure (DRY principle)
- Separate logic into reusable functions

---

# 📈 Portfolio Upgrade Ideas

- Add user authentication
- Add timestamps to posts
- Convert JSON storage → SQLite/PostgreSQL
- Add comments system
- Add pagination
- Add REST API
- Deploy on cloud (Render / Railway / AWS)
- Convert to Django or FastAPI

---

# 🇩🇪 Kurzbeschreibung

Eine einfache Flask-Webanwendung zur Verwaltung von Blogeinträgen.

Die Daten werden in einer JSON-Datei gespeichert und können über eine Weboberfläche erstellt, bearbeitet und gelöscht werden.

---

# 📄 License

MIT License

---

# 👤 Author

Hakan Yildirim  
Python Software Developer (AI Track)  
Masterschool Bootcamp  

GitHub: https://github.com/haki36  
LinkedIn: https://linkedin.com/in/hakan-yildirim-tech
