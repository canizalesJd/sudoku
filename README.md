# 🧩 Sudoku Generator API (Python)

A lightweight Sudoku puzzle generator and API built with pure Python and FastAPI. Designed to be clean, readable, and efficient, with guaranteed unique solutions.

## 📌 Features

- Generates valid 9×9 Sudoku puzzles
- Ensures unique solution
- Exposes a FastAPI endpoint
- Zero heavy dependencies
- Python 3.10+
- Easy to integrate with a frontend

## 🛠️ Tech Stack

- **Language:** Python
- **API:** FastAPI
- **ASGI Server:** Uvicorn
- **Dependency manager:** `uv` (or pip)
- **Libraries:** Python Standard Library + FastAPI

## 📂 Project Structure

```
sudoku/
│
├── main.py              # FastAPI entry point + all Sudoku logic
├── pyproject.toml       # Project configuration
├── requirements.txt     # Dependencies
├── uv.lock              # Dependency lock file
└── README.md            # This file
```

## ▶️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/sudoku.git
cd sudoku
```

### 2️⃣ Verify Python version

```bash
python --version
```

Requires Python 3.10+.

### 3️⃣ Install dependencies

**Using pip:**

```bash
pip install -r requirements.txt
```

**Using uv (recommended):**

```bash
uv sync
```

## 🚀 Running the API

Start the FastAPI server with:

```bash
uvicorn main:app --reload
```

Then open in your browser:

- **API root:** http://127.0.0.1:8000
- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

## 🔌 API Endpoints

### Generate a Sudoku puzzle

```
GET /sudoku
```

**Example Response:**

```json
{
  "puzzle": [
    [0, 3, 0, 0, 7, 0, 0, 0, 0],
    ...
  ],
  "solution": [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    ...
  ]
}
```

### Get service status

```
GET /health
```

**Example Response:**

```json
{
  "status": "ok",
  "service": "sudoku-api"
}
```

## 🧠 Design Notes

- Backtracking-based grid generation
- Early exit solution counting (`limit=2`)
- In-place mutation with controlled deep copies
- Stateless API design (frontend-friendly)
- Lightweight and fast execution

## 🚀 Future Improvements

- Difficulty levels (easy / medium / hard)
- Sudoku solver endpoint
- Puzzle validation endpoint
- Frontend integration (React / Next.js)
- Puzzle persistence

## 👤 Credits

Developed by **Jose Cañizales**

---

## 📄 License

MIT License - feel free to use this project for personal or commercial purposes.