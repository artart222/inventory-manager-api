# Inventory Manager API

A simple inventory management API built with **Django** and **Django REST Framework (DRF)**, using **PostgreSQL** as the database.  

This project demonstrates:

- CRUD operations on products
- Proper API structure using DRF
- Database interaction via Django ORM
- Optional direct PostgreSQL interaction (custom `db.py`) to showcase database knowledge
- Environment-based configuration using `.env`

---

## 🛠 Features

- Create, Read, Update, Delete products via API
- Custom API endpoints for additional operations
- Dynamic URL patterns for flexible API design
- PostgreSQL integration for production-ready usage
- Example of both Django ORM and raw database connection

---

## ⚡ Tech Stack

- Python 3.12  
- Django 5.2.6
- Django REST Framework  
- PostgreSQL
- Psycopg (for raw DB access)  
- python-dotenv (for environment variables)

---

## 📂 Project Structure

```
inventory-manager-api/
├── api/
│ ├── products/
│ │ ├── migrations/
│ │ ├── __init__.py
│ │ ├── models.py
│ │ ├── serializers.py
│ │ ├── views.py
│ │ ├── tests.py
│ │ ├── apps.py
│ │ ├── admin.py
│ │ └── urls.py
│ │
│ ├── manage.py
│ │
│ └── api/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── .env # Environment variables (ignored in git)
├── .gitignore
├── ARCHITECTURE.md
├──  db.py
├──  product.py
├──  main.py
├── requirements.txt
└── README.md
```

---

## ⚙ Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/artart222/inventory-manager-api.git
cd inventory-manager-api
```

2. **Create and activate a virtual environment**

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Create a .env file in the project root**

``` env
SECRET_KEY='your-django-secret-key'
DEBUG=True
DB_NAME='inventory'
DB_USER='postgres'
DB_PASSWORD='password'
DB_HOST='localhost'
DB_PORT='5432'
```

5. **Apply migrations**

```bash
python manage.py migrate
```

6. **Run the development server**
```bash
python manage.py runserver
```

## 🚀 API Endpoints

### Products

| Method | URL                 | Description          |
|--------|---------------------|----------------------|
| GET	   | /api/products/      | List all products    |
| POST	 | /api/products/      | Create a new product |
| GET	   | /api/products/<id>/ | Retrieve a product   |
| PUT	   | /api/products/<id>/ | Update a product     |
| DELETE | /api/products/<id>/ | Delete a product     |

### Example with `curl`

```bash
curl -X POST http://127.0.0.1:8000/api/products/ \
  -H "Content-Type: application/json" \
  -d '{"name":"Car","description":"My car","price":32000,"quantity":15}'
```

## 🔒 Security Notes

Keep SECRET_KEY and database credentials in .env.

Never commit .env to GitHub.

Use DEBUG=False in production and configure ALLOWED_HOSTS.

## 📝 License

MIT License

## 👨‍💻 Author

Artin Mobasher(artart222)
