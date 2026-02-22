# My Website

Academic-style personal site with three pages: **About**, **Research**, and **Blogs**.  
Backend is plain Python (Flask); frontend is HTML and CSS only.

---

## Project structure

```
My-Website/
├── README.md
├── backend/
│   ├── app.py          # Flask app — serves pages, uses frontend for templates & static
│   ├── content.py      # Site content (name, bio, news, publications, patents, blogs)
│   └── requirements.txt
└── frontend/
    ├── templates/      # HTML pages
    │   ├── base.html
    │   ├── about.html
    │   ├── research.html
    │   └── blogs.html
    └── static/
        └── css/
            └── style.css
```

| Folder     | Role |
|-----------|------|
| **backend**  | Python server and data. Edit `content.py` to change copy; run `app.py` to serve the site. |
| **frontend** | All UI: HTML templates and CSS. Edit here to change layout and styling. |

---

## Run locally

1. From the **project root** (`My-Website/`):

   ```bash
   pip install -r backend/requirements.txt
   python backend/app.py
   ```

2. Open **http://127.0.0.1:5000** in your browser.

---

## Pages

| Page      | URL         | Content |
|-----------|-------------|--------|
| **About**   | `/`         | Name, tagline, bio, links, recent news, optional gallery. |
| **Research**| `/research` | Research interests, publications (by year), patents (by year). |
| **Blogs**   | `/blogs`    | List of blog posts with title, date, link, optional excerpt. |

---

## Customize

- **Content** — Edit `backend/content.py`: `NAME`, `BIO`, `LINKS`, `NEWS`, `PHOTOS`, `RESEARCH_INTERESTS`, `PUBLICATIONS`, `PATENTS`, `BLOGS`.
- **Layout** — Edit `frontend/templates/*.html`.
- **Styling** — Edit `frontend/static/css/style.css`.

No database or build step. Change files and refresh the browser.

---

## Deploy to GitHub Pages

The site can be deployed as a **static** version to GitHub Pages (no Python on the server).

### One-time setup

1. In your repo: **Settings → Pages**.
2. Under **Build and deployment**, set **Source** to **GitHub Actions**.

### What’s included

- **`.github/workflows/deploy-pages.yml`** — On every push to `main` or `master`, builds static HTML into `build/` and deploys it to GitHub Pages.
- **`backend/build_static.py`** — Renders all pages with your content and copies assets (CSS, `front.png`) into `build/`. Run locally with:
  ```bash
  BASE_URL=/My-Website python backend/build_static.py
  ```
  (Use your repo name for `BASE_URL`; the workflow sets this automatically.)

### After setup

Push to `main` (or `master`). The **Actions** tab will show the workflow; when it finishes, the site is at:

**https://&lt;username&gt;.github.io/&lt;repo-name&gt;/**

Example: `https://rittik9.github.io/My-Website/`
