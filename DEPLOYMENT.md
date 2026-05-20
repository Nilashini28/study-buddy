# Full Application Deployment Guide

This application consists of 3 parts:
1. **Backend** (FastAPI) → Deploy to Render
2. **Streamlit Frontend** (Python) → Deploy to Streamlit Cloud
3. **React Frontend** (TypeScript/React) → Deploy to Vercel

---

## Part 1: Deploy Backend to Render ✅

### Steps:
1. Go to https://render.com/
2. Sign up / Log in with GitHub
3. Click **"New +"** → **"Web Service"**
4. Connect your GitHub repository: `Nilashini28/study-buddy`
5. Fill in the details:
   - **Name**: `study-buddy-backend`
   - **Root Directory**: `./` (leave empty)
   - **Build Command**: `pip install -r server/requirements.txt`
   - **Start Command**: `cd server && uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Environment**: Python 3.12
   - **Plan**: Free

6. **Add Environment Variables** in Render Dashboard:
   ```
   MONGO_URI=your_mongodb_connection_string
   GROQ_API_KEY=your_groq_api_key
   PINECONE_API_KEY=your_pinecone_api_key
   PINECONE_ENVIRONMENT=your_pinecone_env
   ```

7. Click **"Create Web Service"** and wait for deployment (2-5 minutes)

### Get Your Backend URL:
- After deployment, you'll get a URL like: `https://study-buddy-backend.onrender.com`
- Copy this for the next steps

---

## Part 2: Deploy Streamlit Frontend to Streamlit Cloud ✅

### Steps:
1. Go to https://share.streamlit.io/
2. Sign up / Log in with GitHub
3. Click **"New app"**
4. Fill in:
   - **Repository**: `Nilashini28/study-buddy`
   - **Branch**: `main`
   - **Main file path**: `client/main.py`

5. **Advanced Settings** → Add your Streamlit Secrets:
   ```
   BACKEND_URL = "https://study-buddy-backend.onrender.com"
   ```

6. Click **"Deploy"** and wait for deployment

### Get Your Streamlit URL:
- URL will be: `https://share.streamlit.io/Nilashini28/study-buddy/main/client/main.py`

---

## Part 3: Deploy React Frontend to Vercel ✅

### Steps:
1. Go to https://vercel.com/
2. Sign up / Log in with GitHub
3. Click **"Add New"** → **"Project"**
4. Import your GitHub repository: `Nilashini28/study-buddy`
5. **Framework Preset**: Auto-detect should select Create React App
6. **Configure**:
   - **Build Command**: Already set
   - **Output Directory**: `frontend/build`
   - **Root Directory**: (Leave empty)

7. **Add Environment Variables**:
   ```
   REACT_APP_BACKEND_URL=https://study-buddy-backend.onrender.com
   ```

8. Click **"Deploy"** and wait for deployment (2-5 minutes)

### Get Your Frontend URL:
- URL will be something like: `https://study-buddy.vercel.app`

---

## Part 4: Connect Everything

### Update Frontend Code (if needed):
Make sure your React app uses the `REACT_APP_BACKEND_URL` environment variable:
```javascript
const BACKEND_URL = process.env.REACT_APP_BACKEND_URL || "http://localhost:8000";
```

### Test the Application:
1. Open Streamlit: `https://share.streamlit.io/...`
2. Open React: `https://study-buddy.vercel.app`
3. Test API calls and functionality

---

## Summary of Deployment URLs:
| Service | URL |
|---------|-----|
| Backend API | https://study-buddy-backend.onrender.com |
| Streamlit Frontend | https://share.streamlit.io/Nilashini28/study-buddy/main/client/main.py |
| React Frontend | https://study-buddy.vercel.app |

---

## Troubleshooting:

### Backend Won't Start:
- Check `render.yaml` syntax
- Verify environment variables are set in Render Dashboard
- Check logs in Render Dashboard

### Streamlit Won't Connect:
- Verify `BACKEND_URL` secret is set correctly
- Check that backend is running
- Verify CORS is enabled in FastAPI

### React Won't Connect:
- Check `REACT_APP_BACKEND_URL` environment variable in Vercel
- Verify CORS headers in backend
- Check browser console for errors

---
