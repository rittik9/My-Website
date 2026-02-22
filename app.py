"""
Launcher: run this from project root so templates are found in frontend/.
  python app.py
Or run the backend directly:
  python backend/app.py
"""
import sys
import os

root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(root, "backend"))

from app import app

if __name__ == "__main__":
    app.run(debug=True, port=5000)
