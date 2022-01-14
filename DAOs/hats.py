import sqlite3

from DTOs.hat import hat


class hats:
    def __init__(self,conn):
        self._conn=conn;

    def insert(self,hat):
        self._conn.execute("""
                       INSERT INTO hats (id,topping,supplier,quantity) VALUES (?, ?,?,?)
                   """, [hat.id, hat.topping,hat.supplier,hat.quantity])

    def find(self, topping):
        c = self._conn.cursor()
        c.execute("""
            SELECT id FROM hats WHERE topping = ?
        """, [topping])
        return c.fetchone()


    def get_first_supplierid_of_topping(self,topping):
        c = self._conn.cursor()
        c.execute("""
                  SELECT supplier FROM hats WHERE topping = ?
                  ORDER BY supplier
              """, [topping])
        return c.fetchone()


    def update_toppings_quantity(self,supplier_id,topping):
        c=self._conn.cursor()
        c.execute("""
            UPDATE hats
            SET quantity=quantity-1
            where supplier=? and topping=?
        """, [supplier_id,topping])


    def delete_if_zero(self):
        c = self._conn.cursor()
        c.execute("""
                   DELETE from hats
                   WHERE quantity=0
               """)