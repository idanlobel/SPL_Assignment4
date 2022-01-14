import atexit
import sqlite3
import sys

from DAOs.hats import hats
from DAOs.orders import orders
from DAOs.suppliers import suppliers


class _Repository:
    def __init__(self):
        self._conn = sqlite3.connect(sys.argv[4])
        self.hats = hats(self._conn)
        self.suppliers = suppliers(self._conn)
        self.orders = orders(self._conn)

    def _close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        self._conn.executescript("""
        CREATE TABLE hats (
            id      INT         PRIMARY KEY,
            topping    VARCHAR        NOT NULL,
            supplier   INT         REFERENCES suppliers(id),
            quantity   INT       NOT NULL 
        );

        CREATE TABLE orders (
            id                 INT     PRIMARY KEY,
            location     VARCHAR    NOT NULL,
            hat          INT        REFERENCES hats(id)
        );

        CREATE TABLE suppliers (
            id      INT     PRIMARY KEY ,
            name  VARCHAR     NOT NULL
        );
    """)

    def get_result(self):
        c = self._conn.cursor()
        c.execute("""
                    SELECT hats.topping,suppliers.name,orders.location FROM (hats inner join orders on hats.id=order.hat)inner join suppliers on hats.supplier=suppliers.id
                """)
        return c.fetchall()
    def order_pizza(self):
        c=self._conn.cursor()
        c.execute()
#singelton
repo = _Repository()
atexit.register(repo._close)


