from DTOs.supplier import supplier


class suppliers:
    def __init__(self,conn):
        self._conn=conn;

    def insert(self,supplier):
        self._conn.execute("""
                       INSERT INTO suppliers (id,name) VALUES (?, ?)
                   """, [supplier.id,supplier.name])

    def find(self, supplier_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT name FROM suppliers WHERE id = ?
        """, [supplier_id])
        return supplier(*c.fetchone())