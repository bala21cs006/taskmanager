# 📋 Task Manager — FastAPI + React

A full-stack Task Manager web application built with **FastAPI** (backend) and **React** (frontend).

---

## Project overview

This is a modern, full-stack task management application that allows users to register, authenticate, and manage their personal task lists. The application features a clean and responsive user interface built with React and a robust REST API powered by FastAPI.

### 🌟 Key Features

- ✅ User authentication with JWT tokens
- ✅ Secure password hashing
- ✅ Create, read, update, and delete (CRUD) tasks
- ✅ Mark tasks as complete/incomplete
- ✅ Responsive React UI
- ✅ RESTful API with Swagger documentation
- ✅ CORS enabled for frontend-backend communication
- ✅ SQLite database for data persistence

### 🛠 Tech Stack

**Frontend:**
- React 18
- Axios (HTTP client)
- CSS3 (responsive design)

**Backend:**
- FastAPI (Python web framework)
- SQLAlchemy (ORM)
- SQLite (database)
- JWT (authentication)
- Uvicorn (ASGI server)

---

## Setup instructions

### Prerequisites
- Python 3.8 or higher
- Node.js 14 or higher
- npm or yarn package manager

### Quick Start (Automated)

#### Windows
1. Double-click **`run.bat`** in the project root
2. Wait for both servers to start
3. Open your browser → **http://localhost:3000**

#### Mac / Linux
```bash
chmod +x run.sh && ./run.sh
```

Both the frontend and backend servers will start automatically!

---

### Manual Setup

#### Backend Setup

1. **Navigate to backend directory**
   ```bash
   cd backend
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **Mac/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Create .env file**
   ```bash
   copy .env.example .env      # Windows
   cp .env.example .env        # Mac/Linux
   ```

6. **Run the server**
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```

#### Frontend Setup

1. **Navigate to frontend directory**
   ```bash
   cd frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Create .env file**
   ```bash
   copy .env.example .env      # Windows
   cp .env.example .env        # Mac/Linux
   ```

4. **Start development server**
   ```bash
   npm start
   ```

---

## Environment variables

### Frontend (.env)

```env
REACT_APP_API_URL=http://localhost:8000/api
```

| Variable | Description | Default |
|----------|-------------|---------|
| `REACT_APP_API_URL` | Backend API base URL | `http://localhost:8000/api` |

### Backend (.env)

```env
DATABASE_URL=sqlite:///./taskmanager.db
SECRET_KEY=your-secret-key-here
```

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | Database connection string | `sqlite:///./taskmanager.db` |
| `SECRET_KEY` | Secret key for JWT token generation | Required |

---

## How to run locally

### 1. Start the Backend Server

```bash
cd backend
source venv/bin/activate    # Mac/Linux
# or
venv\Scripts\activate       # Windows

uvicorn app.main:app --reload --port 8000
```

**Backend will be available at:** http://localhost:8000

### 2. Start the Frontend Server (in another terminal)

```bash
cd frontend
npm start
```

**Frontend will open at:** http://localhost:3000

### 3. Access the Application

- **Web App:** http://localhost:3000
- **API Documentation:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

### Usage Example

1. Navigate to http://localhost:3000
2. Click **"Register"** and create a new account
3. Log in with your credentials
4. Click **"Add Task"** to create a new task
5. Use checkboxes to mark tasks as complete
6. Click **"Delete"** to remove tasks

---

## Deployment link

### Local Development URLs

- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:8000
- **API Docs (Swagger):** http://localhost:8000/docs
- **API Docs (ReDoc):** http://localhost:8000/redoc

### Available API Endpoints

#### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login user

#### Tasks
- `GET /api/tasks` - Get all tasks for authenticated user
- `POST /api/tasks` - Create a new task
- `GET /api/tasks/{id}` - Get specific task
- `PUT /api/tasks/{id}` - Update task
- `DELETE /api/tasks/{id}` - Delete task

### Project Structure

```
taskmanager/
├── backend/
│   ├── app/
│   │   ├── core/
│   │   │   └── security.py          # JWT & password hashing
│   │   ├── db/
│   │   │   └── database.py          # Database config
│   │   ├── models/
│   │   │   └── models.py            # SQLAlchemy models
│   │   ├── routers/
│   │   │   ├── auth.py              # Auth endpoints
│   │   │   └── tasks.py             # Task endpoints
│   │   ├── schemas/
│   │   │   └── schemas.py           # Pydantic schemas
│   │   ├── __init__.py
│   │   └── main.py                  # FastAPI app
│   ├── tests/
│   ├── requirements.txt
│   ├── .env.example
│   └── .gitignore
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   │   ├── Login.js
│   │   │   ├── Register.js
│   │   │   └── Dashboard.js
│   │   ├── App.js
│   │   ├── index.js
│   │   └── index.css
│   ├── public/
│   │   └── index.html
│   ├── package.json
│   ├── .env.example
│   └── .gitignore
├── run.bat                  # Windows startup script
├── run.sh                   # Mac/Linux startup script
├── Dockerfile
└── README.md
```

### Troubleshooting

**Port Already in Use:**
```bash
# Windows: Kill process on port
netstat -ano | findstr :3000
taskkill /PID <PID> /F

# Mac/Linux: Kill process on port
lsof -ti:3000 | xargs kill -9
```

**Database Issues:**
```bash
cd backend
rm taskmanager.db        # Remove old database
# Server will create new database on next start
```

**CORS Errors:**
- Ensure both servers are running
- Check `REACT_APP_API_URL` in frontend `.env`
- Verify backend CORS is enabled in `main.py`

---

## 🌐 API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login user

### Tasks
- `GET /api/tasks` - Get all tasks for authenticated user
- `POST /api/tasks` - Create a new task
- `GET /api/tasks/{id}` - Get specific task
- `PUT /api/tasks/{id}` - Update task
- `DELETE /api/tasks/{id}` - Delete task

### Documentation
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

---

## 📂 Project Structure

```
taskmanager/
├── backend/
│   ├── app/
│   │   ├── core/           (security & config)
│   │   ├── db/             (database config)
│   │   ├── models/         (SQLAlchemy models)
│   │   ├── routers/        (API endpoints)
│   │   ├── schemas/        (Pydantic schemas)
│   │   └── main.py         (FastAPI app)
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── pages/          (React components)
│   │   ├── App.js
│   │   ├── index.js
│   │   └── index.css
│   ├── public/
│   └── package.json
├── run.bat                 (Windows launcher)
├── run.sh                  (Mac/Linux launcher)
└── README.md
```

---

## 🚀 Manual Setup (Step by Step)

### Prerequisites
- Python 3.8+
- Node.js 14+
- npm or yarn

### Backend Setup

1. **Navigate to backend directory**
   ```bash
   cd backend
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **Mac/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Create .env file**
   ```bash
   copy .env.example .env      # Windows
   cp .env.example .env        # Mac/Linux
   ```

6. **Run the server**
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```
   - Backend will be available at: http://localhost:8000
   - API Docs: http://localhost:8000/docs

### Frontend Setup

1. **Navigate to frontend directory** (from project root)
   ```bash
   cd frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Create .env file**
   ```bash
   copy .env.example .env      # Windows
   cp .env.example .env        # Mac/Linux
   ```

4. **Start React development server**
   ```bash
   npm start
   ```
   - Frontend will open at: http://localhost:3000

---

## 💡 Usage

### Register & Login
1. Navigate to http://localhost:3000
2. Click "Register" and create a new account
3. Log in with your credentials

### Create Tasks
1. In the Dashboard, enter a task title in the input field
2. Click "Add Task" to create it

### Manage Tasks
- **Mark as complete:** Click the checkbox next to a task
- **Delete task:** Click the "Delete" button

---

## 🐛 Troubleshooting

### Port Already in Use
If port 3000 or 8000 is already in use:
```bash
# Change frontend port in package.json:
"start": "PORT=3001 react-scripts start"

# Change backend port:
uvicorn app.main:app --reload --port 8001
```

### Database Issues
Delete the old database and restart:
```bash
cd backend
del taskmanager.db    # Windows
rm taskmanager.db     # Mac/Linux
```

### CORS Errors
Ensure both servers are running and check the API URL in frontend `.env`

---

## 👤 Author

**Balamurugan E** — Python Developer Intern Submission
