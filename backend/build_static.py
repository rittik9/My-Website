"""
Build static HTML for GitHub Pages. Run from project root:
  python backend/build_static.py
Output goes to build/ (or BUILD_DIR). Set BASE_URL for repo pages, e.g.:
  BASE_URL=/My-Website python backend/build_static.py
"""

import os
import shutil
import sys

# Run from project root; backend/ must be on path for content
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
os.chdir(PROJECT_ROOT)

import content
from jinja2 import Environment, FileSystemLoader

BUILD_DIR = os.path.join(PROJECT_ROOT, "build")
TEMPLATES_DIR = os.path.join(PROJECT_ROOT, "frontend", "templates")
STATIC_DIR = os.path.join(PROJECT_ROOT, "frontend", "static")
BASE_URL = os.environ.get("BASE_URL", "").rstrip("/")


def url_for(endpoint, **kwargs):
    if endpoint == "about":
        return BASE_URL + "/"
    if endpoint == "research":
        return BASE_URL + "/research"
    if endpoint == "blogs":
        return BASE_URL + "/blogs"
    if endpoint == "static" and "filename" in kwargs:
        return BASE_URL + "/static/" + kwargs["filename"]
    if endpoint == "serve_root_file" and "filename" in kwargs:
        return BASE_URL + "/static/" + kwargs["filename"]
    return BASE_URL + "/"


def build():
    if os.path.exists(BUILD_DIR):
        shutil.rmtree(BUILD_DIR)
    os.makedirs(BUILD_DIR)
    os.makedirs(os.path.join(BUILD_DIR, "research"), exist_ok=True)
    os.makedirs(os.path.join(BUILD_DIR, "blogs"), exist_ok=True)

    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    env.globals["url_for"] = url_for

    pub_list = sorted(content.PUBLICATIONS.items(), key=lambda x: x[0], reverse=True)
    patent_list = sorted(content.PATENTS.items(), key=lambda x: x[0], reverse=True)

    # About -> index.html (hero image: full URL or static path)
    hero_fname = getattr(content, "HERO_IMAGE", "front.jpg")
    hero_image_url = getattr(content, "HERO_IMAGE_URL", None) or (BASE_URL + "/static/" + hero_fname)
    env.globals["request"] = type("Req", (), {"endpoint": "about"})()
    t = env.get_template("about.html")
    html = t.render(
        name=content.NAME,
        tagline=content.TAGLINE,
        bio=content.BIO.strip(),
        links=content.LINKS,
        news=content.NEWS,
        photos=content.PHOTOS,
        hero_image_url=hero_image_url,
    )
    with open(os.path.join(BUILD_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

    # Research -> research/index.html
    env.globals["request"] = type("Req", (), {"endpoint": "research"})()
    t = env.get_template("research.html")
    html = t.render(
        research_interests=content.RESEARCH_INTERESTS,
        publications=pub_list,
        patents=patent_list,
    )
    with open(os.path.join(BUILD_DIR, "research", "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

    # Blogs -> blogs/index.html
    env.globals["request"] = type("Req", (), {"endpoint": "blogs"})()
    t = env.get_template("blogs.html")
    html = t.render(blogs=content.BLOGS)
    with open(os.path.join(BUILD_DIR, "blogs", "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

    # Static assets
    shutil.copytree(STATIC_DIR, os.path.join(BUILD_DIR, "static"), dirs_exist_ok=True)
    # Hero image from backend/assets/ (only if not using HERO_IMAGE_URL)
    hero_fname = getattr(content, "HERO_IMAGE", "front.jpg")
    backend_assets_dir = os.path.join(PROJECT_ROOT, "backend", "assets")
    hero_src = os.path.join(backend_assets_dir, hero_fname)
    if not os.path.isfile(hero_src):
        hero_src = os.path.join(PROJECT_ROOT, hero_fname)
    if os.path.isfile(hero_src):
        shutil.copy2(hero_src, os.path.join(BUILD_DIR, "static", hero_fname))

    print("Built static site in", BUILD_DIR)
    print("BASE_URL =", repr(BASE_URL))


if __name__ == "__main__":
    build()
