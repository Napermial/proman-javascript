from flask import Flask, render_template, jsonify, request
import database_common
import data_manager

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def boards():
    if request.method == "POST":
        new_card = request.form["new_card"]
    return render_template('boards.html')


@app.route("/api/boards")
def get_data_boards():
    boards = data_manager.select_board()
    return jsonify(boards)


@app.route("/api/statuses")
def get_data_statuses():
    statuses = data_manager.select_statuses()
    return jsonify(statuses)


@app.route("/api/cards")
def get_data_cards():
    cards = data_manager.select_cards()
    return jsonify(cards)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
