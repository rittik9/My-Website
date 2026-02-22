"""
Site content — edit this file to update your website.
"""

# About
NAME = "Rittik Panda"
TAGLINE = "Research Associate at Multimodal Perception Lab, IIIT Bangalore"
BIO = """
Your main bio paragraph. You can use multiple lines.
Edit this in content.py.
"""

# Links (label -> url)
LINKS = [
    ("Email", "mailto:your.email@example.com"),
    ("Scholar", "https://scholar.google.com"),
    ("LinkedIn", "https://linkedin.com/in/yourusername"),
    ("GitHub", "https://github.com/yourusername"),
    ("CV", "/static/cv.pdf"),
]

# Recent news: list of (date, text)
NEWS = [
    ("Sep 25", "Awarded Outstanding Reviewer at <strong>ICCV 2025</strong>!"),
    ("Jun 25", "Our work on X accepted at <strong>Conference 2025</strong>!"),
    ("Feb 25", "Paper Y and Z accepted at <strong>CVPR 2025</strong>!"),
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
            "venue": "ECCV 2024",
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
