# Deployment Guide for HomeGuard X

This application is ready to be deployed to the cloud. We recommend **Render** as it is free and easiest for Python Flask applications.

## Option 1: Deploy on Render (Recommended)

1.  **Push your code to GitHub**
    - Create a new repository on GitHub.
    - Push the `homeguard_x_web` folder content to it.

2.  **Create a New Web Service on Render**
    - Go to [dashboard.render.com](https://dashboard.render.com/).
    - Click **"New +"** -> **"Web Service"**.
    - Connect your GitHub repository.

3.  **Configure the Service**
    - **Name**: `homeguard-x-demo` (or similar)
    - **Runtime**: `Python 3`
    - **Build Command**: `pip install -r requirements.txt` (Render usually auto-detects this)
    - **Start Command**: `gunicorn app:app` (We created a `Procfile`, so this might also be auto-detected)

4.  **Deploy**
    - Click **"Create Web Service"**.
    - Wait 1-2 minutes. Render will give you a URL like `https://homeguard-x.onrender.com`.

## Option 2: Deploy on Railway

1.  **Login to Railway**
    - Go to [railway.app](https://railway.app/).
2.  **New Project**
    - Click "New Project" -> "Deploy from GitHub repo".
3.  **Select Repo**
    - Choose your `homeguard-x` repository.
4.  **Deploy**
    - Railway automatically detects the `Procfile` and `requirements.txt`.
    - It will be live in minutes.

## Troubleshooting

- **"Module not found" error**: Ensure `requirements.txt` is in the root directory.
- **Port errors**: Render/Railway injects a `PORT` environment variable. Our `gunicorn` command handles this automatically.
