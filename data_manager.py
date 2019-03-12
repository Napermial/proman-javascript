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
