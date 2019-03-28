import database_common
from psycopg2 import sql

@database_common.connection_handler
def select_board(cursor):
    cursor.execute("""
                     SELECT * FROM boards;
                      """,
                   )
    boards = cursor.fetchall()
    return boards


@database_common.connection_handler
def select_statuses(cursor):
    cursor.execute("""
    
                     SELECT * FROM statuses;
                      """,
                   )
    statuses = cursor.fetchall()
    return statuses


@database_common.connection_handler
def select_cards(cursor):
    cursor.execute("""
                     SELECT * FROM cards;
                      """,
                   )
    cards = cursor.fetchall()
    return cards


@database_common.connection_handler
def add_new_card(cursor, new_card, board_id):
    cursor.execute("""
                     INSERT INTO cards(title, board_id, status_id, order_)
                     VALUES (%(new_card)s, %(board_id)s, 1, 1)
                      """, {'new_card': new_card, 'board_id': board_id})