# FastAPI JWT Auth + RBAC API

This project is a FastAPI-based REST API with JWT authentication and Role-Based Access Control (RBAC) using PostgreSQL and SqlModel.

## 🔧 Features

- ✅ User Registration & Login
- 🔐 JWT-based Authentication
- 👮 Role-Based Access Control (Admin/User)
- 📁 CRUD for Projects (Admin can Create, Update, Delete; Users can Read)
- 🗄️ PostgreSQL + SqlModel ORM

---

## 🚀 Setup Instructions

### 1. Clone the Repo & Create Virtual Env

```bash
git clone https://github.com/yourname/fastapi-rbac-jwt.git
cd fastapi-rbac-jwt
python -m venv venv
source venv/bin/activate
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

Create a `.env` file (already included in template):

```
DATABASE_URL=postgresql://username:password@localhost:5432/yourdbname
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Make sure PostgreSQL is running and the DB is created.

### 4. Run the App

```bash
uvicorn app.main:app --reload
```

---

## 🛠️ API Endpoints

### Auth

- `POST /register` - Register new user
```json
{
  "username": "user1",
  "password": "pass123",
  "role": "user"
}
```

- `POST /login` - Get JWT token
```json
{
  "username": "user1",
  "password": "pass123"
}
```

### Projects

- `GET /projects` - Get list of projects (user/admin)
- `POST /projects` - Create a project (admin only)
```json
{
  "name": "Project Alpha",
  "description": "This is a sample project"
}
```

---

## 📽️ Demo Video

📌 Record using Loom/OBS and showcase:
- Registering new users
- Logging in to get JWT
- Using JWT in Postman to access role-based endpoints

---

## 📚 Tech Stack

- **FastAPI** ⚡
- **PostgreSQL** 🐘
- **SqlModel** 🧱
- **JWT (python-jose)** 🔐
- **Passlib** 🔑
- **Dotenv** 🌱

---

## 🤝 License

Free to use for learning and demo purposes.

---

Made with ❤️ by [Your Name]
