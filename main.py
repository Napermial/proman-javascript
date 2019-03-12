from flask import Flask, render_template, jsonify
import database_common
import data_manager

app = Flask(__name__)


@app.route("/")
def boards():
    ''' this is a one-pager which shows all the boards and cards '''
    return render_template('boards.html')

@app.route("/api/boards")
def get_data_boards():
    boards = data_manager.select_board()
    return jsonify(boards)


@app.route("/api/statuses")
def get_data_statuses():
    statuses = data_manager.select_statuses()
    return jsonify(statuses)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
