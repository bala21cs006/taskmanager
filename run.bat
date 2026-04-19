@echo off
echo ============================================
echo   Task Manager - Setup and Run (Windows)
echo ============================================

REM Setup Backend
cd /d "%~dp0backend"

echo.
echo [1/6] Creating virtual environment...
python -m venv venv

echo.
echo [2/6] Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo [3/6] Installing backend dependencies...
pip install -r requirements.txt

echo.
echo [4/6] Creating .env if not exists...
if not exist .env (
    copy .env.example .env
    echo .env created from .env.example
) else (
    echo .env already exists, skipping.
)

REM Setup Frontend
cd /d "%~dp0frontend"

echo.
echo [5/6] Installing frontend dependencies...
call npm install

echo.
echo [6/6] Creating frontend .env if not exists...
if not exist .env (
    copy .env.example .env
    echo .env created from .env.example
) else (
    echo .env already exists, skipping.
)

echo.
echo ============================================
echo   Starting servers...
echo ============================================
echo   Frontend: http://localhost:3000
echo   Backend:  http://localhost:8000
echo   API Docs: http://localhost:8000/docs
echo.
echo   Press Ctrl+C in each window to stop
echo ============================================
echo.

REM Start backend in a new window
cd /d "%~dp0backend"
call venv\Scripts\activate.bat
start "Task Manager - Backend" cmd /k uvicorn app.main:app --reload --port 8000

REM Wait a second for backend to start
timeout /t 2 /nobreak

REM Start frontend in a new window
cd /d "%~dp0frontend"
start "Task Manager - Frontend" cmd /k npm start
