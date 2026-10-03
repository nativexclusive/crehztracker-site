# crehztracker.com

The marketing site for CrehzTracker. Plain static files: `index.html`, `tutorials.html`, `site.css`, `fonts.css`, `img/`, `media/`.

Hosted with IONOS Deploy Now. Every push to `main` redeploys. The repo root is the web root — no build step.

`_tint.py` re-tints the App Store screenshots into the app's palettes; it needs the project checkout and Pillow and is not run on deploy.

When the app is on the App Store, set `APP_STORE_URL` at the bottom of both pages.
