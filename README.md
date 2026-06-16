# 📝 Full-Stack Blogging Website

[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/fastapi-0.104+-green.svg)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

A modern, full-stack blogging platform built with **Python (FastAPI)**, **SQLite/PostgreSQL**, and **Jinja2 templates**. Features user authentication, markdown support, and a clean responsive design.

## ✨ Features

- 🔐 **User Authentication** - Register, login, and secure sessions
- 📝 **Create & Edit Posts** - Write blog posts with markdown support
- 👤 **Author Profiles** - Each post shows the author's information
- 🎨 **Responsive Design** - Works perfectly on desktop, tablet, and mobile
- 🚀 **Fast & Modern** - Built with FastAPI for high performance
- 💾 **Database Ready** - SQLite for development, PostgreSQL for production
- 🔍 **SEO Friendly** - Clean URLs and semantic HTML

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| FastAPI | Backend framework |
| SQLAlchemy | ORM for database |
| Jinja2 | Template engine |
| SQLite/PostgreSQL | Database |
| Python-Markdown | Markdown rendering |
| JWT + Bcrypt | Authentication |

## 🚀 Quick Start

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)

### Installation

```bash
# Clone the repository
git clone https://github.com/pallavi-dhadage/blogging-website.git
cd blogging-website

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Edit .env and add your SECRET_KEY

# Initialize database
python -c "from app.database import engine, Base; from app import models; Base.metadata.create_all(bind=engine)"

# Run the application
uvicorn app.main:app --reload
