# Nairim's Cuties – Flask Web Application

A dynamic web application built with Flask for a children's clothing brand called Nairim's Cuties.
The app displays a product catalogue, individual product details, brand information, and a contact form.

---

## Live Demo

The application is deployed on Render and accessible at:
https://module2-python-project.onrender.com

---

## Features

- **Home page** – Hero section with tagline and featured product picks
- **Shop page** – Full product catalogue rendered from a Python data structure, with a sale badge and strikethrough pricing for discounted items
- **Product detail page** – Dynamic route (`/product/<id>`) displaying individual product information including name, price, category, and age range
- **About page** – Brand story and values
- **Contact page** – Contact form with POST method handling and server-side processing

---

## Tech Stack

- Python 3.13
- Flask 3.1.3
- Jinja2 (template engine)
- HTML5 / CSS3
- Gunicorn (production server)
- uv (package manager)
- Deployed on Render.com

---

## Project Structure
static, templates, app.py, pyproject.toml, .gitignore, README.md, uv.lock

---

## How to Run Locally

**1. Clone the repository:**
```bash
git clone https://github.com/LilianAtaide/Module2_python_project
cd Module2_python_project
```

**2. Install dependencies:**
```bash
uv sync
```

**3. Run the development server:**
```bash
uv run app.py
```

**4. Open in your browser:**

---

## How to Run Locally

**1. Clone the repository:**
```bash
git clone https://github.com/LilianAtaide/Module2_python_project
cd Module2_python_project
```

**2. Install dependencies:**
```bash
uv sync
```

**3. Run the development server:**
```bash
uv run app.py
```

**4. Open in your browser:**

http://127.0.0.1:5000

---

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `SECRET_KEY` | Flask secret key for session security | Yes (on production) |

On Render this is set via the Environment tab in the service dashboard.
Locally, the app falls back to a development key automatically.

---

## Deployment on Render

1. Push the project to GitHub
2. Create a new **Web Service** on [Render.com](https://render.com)
3. Connect the GitHub repository
4. Set the following:
   - **Build command:** `uv sync`
   - **Start command:** `gunicorn app:app`
   - **Environment variable:** `SECRET_KEY` = your chosen secret string
5. Click **Deploy** — Render will build and launch the app automatically

---

## Dynamic Features Demonstrated

- Python list of dictionaries passed into Jinja2 templates
- `{% for %}` loop rendering the product catalogue
- `{% if %}` conditional displaying a sale badge and strikethrough price
- Dynamic URL route `/product/<int:product_id>` loading per-product data
- Contact form using `POST` method with server-side field processing