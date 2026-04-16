# CastMate PWA — Deployment Guide

A fully installable Pacific Northwest fishing companion app.  
Runs on iPhone, Android, or any browser. No app store needed.

---

## What's in this folder

```
castmate-pwa/
└── public/
    ├── index.html      ← The entire app (React + all logic, self-contained)
    ├── manifest.json   ← PWA install metadata
    ├── sw.js           ← Service worker (offline support)
    ├── icon-192.png    ← App icon
    └── icon-512.png    ← App icon (large)
```

---

## Deploy to Netlify (free, ~2 minutes)

1. Go to **https://netlify.com** and sign up (free)
2. From the dashboard, click **"Add new site" → "Deploy manually"**
3. Drag the **`public/` folder** into the upload box
4. Netlify gives you a URL like `https://castmate-xyz.netlify.app`
5. Done — open that URL on your phone!

---

## Install on iPhone (Safari)

1. Open the Netlify URL in **Safari** (must be Safari, not Chrome)
2. Tap the **Share** button (box with arrow)
3. Scroll down and tap **"Add to Home Screen"**
4. Tap **"Add"** — CastMate appears on your home screen like a native app

## Install on Android (Chrome)

1. Open the Netlify URL in **Chrome**
2. Tap the **three-dot menu** (⋮) in the top right
3. Tap **"Add to Home Screen"** or **"Install App"**
4. Tap **"Install"** — done!

---

## Features that work as a PWA

| Feature | Browser | Installed PWA |
|---|---|---|
| GPS / live location | ✅ | ✅ (better accuracy) |
| Camera / photo capture | ✅ | ✅ (direct camera) |
| AI fish identification | ✅ | ✅ |
| Offline map view | ❌ | ✅ (cached) |
| Full-screen no browser chrome | ❌ | ✅ |
| Home screen icon | ❌ | ✅ |

---

## Updating the app

1. Edit `public/index.html`
2. Change `const CACHE = "castmate-v1"` → `"castmate-v2"` in `sw.js`  
   (this forces phones to refresh the cached version)
3. Re-drag the `public/` folder to Netlify

---

## Notes

- **All data is local** — catches, gear, and profile are saved in the browser's localStorage on each device
- **AI features require internet** — the Anthropic API calls need a connection
- **The app works offline** for viewing existing catches and gear once loaded
- Icons are minimal placeholders — replace `icon-192.png` and `icon-512.png` with your own artwork for a polished look (must be square PNGs)
