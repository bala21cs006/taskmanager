#!/bin/bash
echo "============================================"
echo "  Task Manager - Setup and Run (Mac/Linux)"
echo "============================================"

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Setup Backend
cd "$SCRIPT_DIR/backend"

echo ""
echo "[1/6] Creating virtual environment..."
python3 -m venv venv

echo ""
echo "[2/6] Activating virtual environment..."
source venv/bin/activate

echo ""
echo "[3/6] Installing backend dependencies..."
pip install -r requirements.txt

echo ""
echo "[4/6] Creating .env if not exists..."
if [ ! -f .env ]; then
    cp .env.example .env
    echo ".env created from .env.example"
else
    echo ".env already exists, skipping."
fi

# Setup Frontend
cd "$SCRIPT_DIR/frontend"

echo ""
echo "[5/6] Installing frontend dependencies..."
npm install

echo ""
echo "[6/6] Creating frontend .env if not exists..."
if [ ! -f .env ]; then
    cp .env.example .env
    echo ".env created from .env.example"
else
    echo ".env already exists, skipping."
fi

echo ""
echo "============================================"
echo "   Starting servers..."
echo "============================================"
echo "   Frontend: http://localhost:3000"
echo "   Backend:  http://localhost:8000"
echo "   API Docs: http://localhost:8000/docs"
echo ""
echo "   Press Ctrl+C to stop all servers"
echo "============================================"
echo ""

# Start backend
cd "$SCRIPT_DIR/backend"
source venv/bin/activate
echo "Starting backend server..."
uvicorn app.main:app --reload --port 8000 &
BACKEND_PID=$!

# Wait for backend to start
sleep 2

# Start frontend
cd "$SCRIPT_DIR/frontend"
echo "Starting frontend server..."
npm start &
FRONTEND_PID=$!

# Wait for both to complete
wait $BACKEND_PID $FRONTEND_PID
