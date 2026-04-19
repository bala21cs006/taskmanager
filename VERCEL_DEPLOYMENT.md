# Deployment Guide - Vercel Full-Stack Deployment

## Prerequisites
1. **Vercel Account** - Sign up at https://vercel.com
2. **GitHub Account** - Push your code to GitHub
3. **Node.js & npm** - For local testing

## Deployment Steps

### Step 1: Push to GitHub
```bash
git init
git add .
git commit -m "Ready for Vercel deployment"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/task-manager.git
git push -u origin main
```

### Step 2: Connect to Vercel
1. Go to https://vercel.com/new
2. Select "Import Git Repository"
3. Find and import your `task-manager` repository
4. Click "Import"

### Step 3: Configure Project Settings
1. **Framework Preset**: Select "Other" (custom)
2. **Build Command**: `cd frontend && npm install && npm run build`
3. **Output Directory**: `frontend/build`
4. **Install Command**: `npm install` (in root if needed)

### Step 4: Environment Variables
In the Vercel dashboard, add these under "Environment Variables":

**For Development/Preview:**
```
REACT_APP_API_URL = https://your-project.vercel.app/api
```

**For Production:**
```
REACT_APP_API_URL = https://your-project.vercel.app/api
```

### Step 5: Deploy
1. Click "Deploy"
2. Wait for build completion (~2-3 minutes)
3. Your app will be live at `https://your-project.vercel.app`

## Testing the Deployment

### Frontend
```bash
curl https://your-project.vercel.app
```

### Backend API
```bash
curl https://your-project.vercel.app/api/docs
```

## Post-Deployment Setup

### Database Setup (One-time)
Since this uses SQLite, you'll need to use a cloud database. Update `.env` in Vercel with:

```
DATABASE_URL=your-cloud-db-connection-string
```

Then modify `backend/app/db/database.py` to use PostgreSQL:

```python
from sqlalchemy import create_engine
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
engine = create_engine(DATABASE_URL)
```

### Recommended Cloud Databases:
- **PostgreSQL**: Railway, Render, Supabase
- **MongoDB**: MongoDB Atlas
- **MySQL**: PlanetScale

## Troubleshooting

### API calls failing
- Check browser DevTools Console
- Verify `REACT_APP_API_URL` environment variable is set correctly
- Ensure CORS is enabled in backend

### Build fails
- Check Vercel Build Logs
- Ensure all dependencies are in `package.json` and `requirements.txt`
- Verify Python version compatibility (using 3.11)

### Database errors
- Verify connection string format
- Check database credentials
- Ensure database allows remote connections

## Rollback
To rollback to a previous deployment:
1. Go to Vercel Dashboard → Deployments
2. Click the deployment you want to restore
3. Click the three-dot menu → "Redeploy"

## Need Help?
- Vercel Docs: https://vercel.com/docs
- FastAPI Docs: https://fastapi.tiangolo.com/
- React Docs: https://react.dev/
