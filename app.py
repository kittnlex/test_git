from flask import Flask, jsonify, request, abort

app = Flask(__name__)

books = []
next_id = 1

# comments
def find_book(book_id):
    return next((b for b in books if b["id"] == book_id), None)

# practicing with comments
@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(books), 200

# test git
@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = find_book(book_id)
    if book is None:
        abort(404)
    return jsonify(book), 200

# Miau Miau different text
@app.route("/books", methods=["POST"])
def create_book():
    global next_id
    data = request.get_json()

    if not data:
        abort(400)

    required = {"title", "author", "year"}
    missing = required - data.keys()
    if missing:
        return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400

    book = {
        "id": next_id,
        "title": data["title"],
        "author": data["author"],
        "year": data["year"],
    }
    books.append(book)
    next_id += 1
    return jsonify(book), 201

@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    book = find_book(book_id)
    if book is None:
        abort(404)

    data = request.get_json()
    if not data:
        abort(400)

    for field in ("title", "author", "year"):
        if field in data:
            book[field] = data[field]

    return jsonify(book), 200

# Teammates work
#bla bla bla
@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = find_book(book_id)
    if book is None:
        abort(404)

    books.remove(book)
    return "", 204


if __name__ == "__main__":
    app.run(debug=True)
