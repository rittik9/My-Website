"""
Site content — edit this file to update your website.
"""

# About
NAME = "Rittik Panda"
TAGLINE = "Research Associate at Multimodal Perception Lab, IIIT Bangalore"
# Hero image: use EITHER a filename in backend/assets/ OR a full URL.
# Option A: filename (served from backend/assets/ or built into static/)
HERO_IMAGE = "front.png"
# Option B: full URL (image loads from this URL; use if file not found locally)
# Uncomment and set to your raw GitHub URL so the image always shows:
HERO_IMAGE_URL = "https://raw.githubusercontent.com/rittik9/My-Website/master/backend/assets/front.png"
BIO = ""

# """
# Your main bio paragraph. You can use multiple lines.
# Edit this in content.py.
# """

EMAIL = "your.email@example.com"

# Links (label -> url)
LINKS = [
    ("Scholar", "https://scholar.google.com"),
    ("GitHub", "https://github.com/rittik9"),
    ("X", "https://x.com/rittik_panda"),
    ("LinkedIn", "https://www.linkedin.com/in/rittik-panda-752143169/"),
    ("CV", "/static/cv.pdf"),
]

# Recent news: list of (date, text)
NEWS = [
    ("Sep 25", "Awarded Outstanding Reviewer at <strong>Conference 2025</strong>!"),
    ("Jun 25", "Our work on X accepted at <strong>Conference 2025</strong>!"),
    ("Feb 25", "Paper Y and Z accepted at <strong>Conference 2025</strong>!"),
]

# Publications: year -> list of {title, authors, venue, project_url, paper_url, code_url}
PUBLICATIONS = {
    "2025": [
        {
            "title": "Your Paper Title Here",
            "authors": "You*, Co-author, Advisor",
            "venue": "Conference 2025",
            "project_url": "#",
            "paper_url": "#",
            "code_url": "#",
        },
    ],
    "2024": [
        {
            "title": "Another Paper",
            "authors": "You, Others",
            "venue": "Conference 2025",
            "project_url": "#",
            "paper_url": "#",
            "code_url": None,
        },
    ],
}

# Optional: gallery images (path under static/)
PHOTOS = []  # e.g. ["img/photo1.jpg", "img/photo2.jpg"]

# Research page
RESEARCH_INTERESTS = [
    "Your first research interest area (e.g. Computer Vision, Generative Models).",
    "Second area (e.g. Controllable Image Editing, Diffusion Models).",
    "Third area if any.",
]

# Patents: year -> list of {title, inventors, number_or_status, url (optional)}
PATENTS = {
    "2024": [
        {
            "title": "Method for Example Invention",
            "inventors": "You, Co-inventor, Others",
            "number_or_status": "US 12,345,678",
            "url": "#",
        },
    ],
    "2023": [
        {
            "title": "Another Patent",
            "inventors": "You, Others",
            "number_or_status": "Pending",
            "url": None,
        },
    ],
}

# Blogs: list of {title, date, url, excerpt (optional)}
BLOGS = [
    {
        "title": "Your First Blog Post",
        "date": "Jan 2025",
        "url": "https://medium.com/...",
        "excerpt": "Short summary or first line of the post.",
    },
    {
        "title": "Another Post",
        "date": "Nov 2024",
        "url": "#",
        "excerpt": "Optional excerpt.",
    },
]
