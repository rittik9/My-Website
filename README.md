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
