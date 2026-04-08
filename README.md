# Bookshelf API

A simple REST API for managing a bookshelf, built with Flask.

## Setup

### 1. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the server

```bash
python app.py
```

The API will be available at `http://127.0.0.1:5000`.

---

## Endpoints

### List all books
```
GET /books
```

### Get a book by ID
```
GET /books/<id>
```

### Add a new book
```
POST /books
Content-Type: application/json

{
  "title": "The Pragmatic Programmer",
  "author": "David Thomas",
  "year": 1999
}
```

### Update a book
```
PUT /books/<id>
Content-Type: application/json

{
  "year": 2019
}
```

### Delete a book
```
DELETE /books/<id>
```

---

## Book schema

| Field    | Type    | Description          |
|----------|---------|----------------------|
| `id`     | integer | Auto-assigned ID     |
| `title`  | string  | Title of the book    |
| `author` | string  | Author's name        |
| `year`   | integer | Publication year     |

## Notes

- Storage is in-memory; data resets on server restart.
