"""
Flask backend — serves About, Research, and Blogs pages.
Templates and static files are in the frontend folder.
Run from project root: python backend/app.py
Then open http://127.0.0.1:5000
"""

import os

from flask import Flask, render_template, send_from_directory, url_for

import content

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
FRONTEND_DIR = os.path.join(PROJECT_ROOT, "frontend")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

app = Flask(
    __name__,
    template_folder=os.path.join(FRONTEND_DIR, "templates"),
    static_folder=os.path.join(FRONTEND_DIR, "static"),
)


@app.context_processor
def inject_name():
    return {"name": content.NAME}


@app.route("/assets/<path:filename>")
def serve_assets(filename):
    """Serve files from backend/assets/ (e.g. front.png)."""
    return send_from_directory(ASSETS_DIR, filename)


@app.route("/")
def about():
    return render_template(
        "about.html",
        tagline=content.TAGLINE,
        bio=content.BIO.strip(),
        email= content.EMAIL,
        links=content.LINKS,
        news=content.NEWS,
        photos=content.PHOTOS,
        hero_image_url=getattr(content, "HERO_IMAGE_URL", None) or url_for("serve_assets", filename=getattr(content, "HERO_IMAGE", "front.jpg")),
    )


@app.route("/research")
def research():
    pub_list = sorted(
        content.PUBLICATIONS.items(),
        key=lambda x: x[0],
        reverse=True,
    )
    patent_list = sorted(
        content.PATENTS.items(),
        key=lambda x: x[0],
        reverse=True,
    )
    return render_template(
        "research.html",
        research_interests=content.RESEARCH_INTERESTS,
        publications=pub_list,
        patents=patent_list,
    )


@app.route("/blogs")
def blogs():
    return render_template("blogs.html", blogs=content.BLOGS)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
