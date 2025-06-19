# Personal Knowledge Base Web Application

This repository contains a Flask-based web application designed to serve as a personal knowledge base. It is structured to support modular development using Flask blueprints and is optimized for deployment on Vercel as serverless functions.

## Features

* **Modular Architecture**: Organized with Flask blueprints to separate concerns (e.g., `home`, `users`, etc.).
* **Serverless Deployment**: Configured for Vercel using `vercel.json` and `@vercel/python` runtime.
* **Static Asset Management**: CSS and JavaScript assets served from a `static/` directory.
* **Environment Configuration**: Supports multiple environments via `.flaskenv` and `.env` files.

## Table of Contents

- [Personal Knowledge Base Web Application](#personal-knowledge-base-web-application)
  - [Features](#features)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Project Structure](#project-structure)
  - [Local Development](#local-development)
  - [Deployment to Vercel](#deployment-to-vercel)
  - [Adding New Endpoints](#adding-new-endpoints)
  - [Contributing](#contributing)
  - [License](#license)
    - [TL;DR](#tldr)

## Prerequisites

* Python 3.8+
* [pip](https://pip.pypa.io/) or a compatible package manager
* (Optional) Vercel CLI for local testing:

  ```bash
  npm install -g vercel
  ```

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/personal-knowledge.git
   cd personal-knowledge
   ```
2. **Create and activate a virtual environment**:

   ```bash
   python -m venv .venv
   source .venv/bin/activate    # macOS/Linux
   .\.venv\\Scripts\\activate  # Windows PowerShell
   ```
3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

* **`.flaskenv`** (tracked)

  ```dotenv
  FLASK_APP=api/index.py
  FLASK_ENV=development
  FLASK_DEBUG=1
  ```
* **`.env`** (ignored)

  ```dotenv
  SECRET_KEY=your-secret-key
  DATABASE_URL=sqlite:///data.db
  ```

## Project Structure

```text
personal-knowledge/
├── api/                          # Serverless functions for Vercel
│   ├── __init__.py               # Package marker
│   ├── index.py                  # App factory & blueprint registration
│   ├── config.py                 # Environment-specific configs
│   ├── extensions.py             # Initialize DB, CORS, etc.
│   └── blueprints/               # Feature-based route modules
├── models/                       # ORM models or Pydantic schemas
├── static/                       # CSS, JavaScript, images
│   ├── css/
│   └── js/
├── templates/                    # Jinja2 HTML templates
├── utils/                        # Helper modules and utilities
├── requirements.txt              # Python dependencies
├── .flaskenv                     # Flask CLI environment variables
├── .env                          # Sensitive env variables (ignored)
├── vercel.json                   # Vercel build & routing configuration
└── README.md                     # This file
```

## Local Development

1. **Run the Flask server**:

   ```bash
   export FLASK_APP=api/index.py
   export FLASK_ENV=development
   flask run
   ```
2. **Access in browser**: Navigate to `http://127.0.0.1:5000/`
3. **Hot reloading**: Enabled by `FLASK_ENV=development` for automatic code reloads.

## Deployment to Vercel

1. **Login and initialize**:

   ```bash
   vercel login
   vercel init   # choose “Other” framework preset if prompted
   ```
2. **Add `vercel.json`** (already included):

   ```json
   {
     "version": 2,
     "builds": [
       { "src": "api/**/*.py", "use": "@vercel/python" }
     ],
     "routes": [
       { "src": "/static/(.*)", "dest": "/static/$1" },
       { "src": "/(.*)",        "dest": "api/index.py" }
     ]
   }
   ```
3. **Deploy**:

   ```bash
   vercel --prod
   ```

## Adding New Endpoints

* **Blueprint pattern**:

  1. Create a new folder under `api/blueprints/<feature>/`
  2. Add `__init__.py` and `routes.py`
  3. Define your routes with `@blueprint.route(...)`
  4. Register the blueprint in `api/index.py`

Example:

```python
# api/blueprints/blog/routes.py
from flask import Blueprint, render_template

blog_bp = Blueprint('blog', __name__, url_prefix='/blog')

@blog_bp.route('/')
def list_posts():
    return render_template('blog/list.html')
```

## Contributing

* Fork the repository and create a feature branch.
* Submit a pull request with clear descriptions and tests.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

### TL;DR

* Modular Flask app with blueprints under `api/blueprints/`.
* Static files in `static/`, templates in `templates/`.
* Local dev via `flask run`, deploy with `vercel --prod` using `vercel.json`.
* Add new endpoints by creating blueprints and registering them in `index.py`.
