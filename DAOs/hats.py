import sqlite3

from DTOs.hat import hat


class hats:
    def __init__(self,conn):
        self._conn=conn;

    def insert(self,hat):
        self._conn.execute("""
                       INSERT INTO hats (id,topping,supplier,quantity) VALUES (?, ?,?,?)
                   """, [hat.id, hat.topping,hat.supplier,hat.quantity])

    def find(self, hat_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT topping FROM students WHERE id = ?
        """, [hat_id])
        return hat(*c.fetchone())