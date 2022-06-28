import sqlite3

with sqlite3.connect("netflix.db") as connection:
    connection.row_factory = sqlite3.Row
    result = connection.execute(
        f'''
    select *
    from netflix
    '''
    ).fetchall()

    print(result)
