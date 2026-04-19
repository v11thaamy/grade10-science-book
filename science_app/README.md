# Grade 10 Science Book
### Holy Angel English School, Pokhara, Nepal

A free, permanent web app — works on laptop AND phone, anytime, anywhere.

---

## DEPLOY IN 5 STEPS (Free Forever)

### WHAT YOU NEED:
- GitHub account (free) → github.com
- Render account (free) → render.com
- Your Anthropic API key

---

### STEP 1 — Upload to GitHub

1. Go to **github.com** and sign in (or create free account)
2. Click the **"+"** button (top right) → **"New repository"**
3. Repository name: `grade10-science-book`
4. Make it **Public**
5. Click **"Create repository"**
6. On the next page, click **"uploading an existing file"**
7. Drag and drop ALL these files:
   - `app.py`
   - `requirements.txt`
   - `render.yaml`
   - `static/index.html`  ← (upload the static folder too)
8. Click **"Commit changes"**

---

### STEP 2 — Deploy on Render (Free Hosting)

1. Go to **render.com** and sign in with your GitHub account
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository: `grade10-science-book`
4. Render auto-detects settings from `render.yaml`
5. Click **"Create Web Service"**

---

### STEP 3 — Add Your API Key

1. In Render dashboard, go to your service
2. Click **"Environment"** tab
3. Click **"Add Environment Variable"**
4. Key: `ANTHROPIC_API_KEY`
5. Value: your Anthropic API key (starts with `sk-ant-...`)
6. Click **"Save Changes"**
7. Service restarts automatically

---

### STEP 4 — Get Your Link

After deployment (takes 2-3 minutes):
- Render gives you a free link like:
  `https://grade10-science-book.onrender.com`
- **Bookmark this on your laptop AND phone!**

---

### STEP 5 — Done!

✅ Open on laptop browser  
✅ Open on phone browser  
✅ Works 24/7 without your laptop being on  
✅ Free forever  
✅ Share with other teachers too!

---

## NOTES

- **Free tier**: Render free tier "sleeps" after 15 min of no use.
  First load after sleep takes ~30 seconds. This is normal!
- To keep it always awake, use a free service like uptimerobot.com
  to ping your app every 10 minutes.

---

## FILES EXPLAINED

| File | Purpose |
|------|---------|
| `app.py` | Python Flask server — handles API calls |
| `requirements.txt` | Python packages needed |
| `render.yaml` | Tells Render how to deploy |
| `static/index.html` | The full Science Book app |

---

*Made for Holy Angel English School, Pokhara-09, Kaski, Nepal*
