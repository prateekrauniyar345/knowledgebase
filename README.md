## Repo Structure
personal-knowledge/
├── api/                          ← Vercel Serverless functions
│   ├── __init__.py               # makes `api` a Python package
│   ├── index.py                  # entry‐point: creates & exports your Flask `app`
│   ├── config.py                 # dev/prod/testing configs
│   ├── extensions.py             # init DB, CORS, auth, etc.
│   └── blueprints/               # one folder per feature
│       ├── home/
│       │   ├── __init__.py       # defines `home_bp`
│       │   └── routes.py         # `@home_bp.route("/")`
│       ├── users/
│       │   ├── __init__.py       # defines `users_bp`
│       │   └── routes.py         # `@users_bp.route("/users")`
│       └── …                      # additional blueprints
├── models/                       # ORM models or Pydantic schemas
├── static/                       # served by Flask & Vercel
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── index.js
├── templates/                    # Jinja2 HTML templates
│   ├── root.html
│   └── home.html
├── utils/                        # helper modules
├── requirements.txt              # `flask`, `python-dotenv`, etc.
├── .flaskenv                     # FLASK_APP, FLASK_ENV, FLASK_DEBUG
├── .env                          # secret keys, database URLs
├── vercel.json                   # Vercel build & routing config
└── README.md
