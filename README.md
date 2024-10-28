# 📚 FastAPI REST API with PostgreSQL, Alembic, and Pytest

This repository provides a guide to building a REST API using FastAPI, with PostgreSQL for data storage, Alembic for migrations, and Pytest for testing.

## ⚙️ Key Features
- 🔑 User Authentication: Secure OAuth2 and JWT-based authentication.
- 📋 CRUD Operations: Comprehensive create, read, update, delete functionality for users and posts.
- 📊 Voting System: Allows users to vote on posts.
- 📈 Database Migrations: Managed with Alembic for seamless updates.

## 🛠️ Setup

1. Clone the repository:
``` bash
git clone https://github.com/VirajBhagiya/API-tutorial.git
cd API-tutorial
```

2. Create a virtual environment:
``` bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
``` bash
pip install -r requirements.txt
```

4. Configure environment variables in a .env file:
``` bash
DATABASE_URL=postgresql://user:password@localhost/db_name
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

5. Run migrations:
``` bash
alembic upgrade head
```


## 🚀 Running the API

Start the FastAPI server:
``` bash
uvicorn app.main:app --reload
```

API available at http://127.0.0.1:8000.

## 🔍 Testing

Run tests using `pytest`:
```bash
pytest
```

# 🤝 Contributions
Contributions are welcome! Please follow these steps:

- Fork the repository.
- Create a new branch.
- Commit your changes.
- Push to the branch.
- Open a pull request.

Happy building! 🛠️