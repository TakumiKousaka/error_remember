"""
A Sample Web-DB Application for DB-DESIGN lecture
Copyright (C) 2022 Yasuhiro Hayashi
"""
from psycopg2 import sql, connect, ProgrammingError
import flaskdb.var as v
from flaskdb.models import Item, Error

class DataAccess:

    # Constractor called when this class is used. 
    # It is set for hostname, port, dbname, useranme and password as parameters.
    def __init__(self, hostname, port, dbname, username, password):
        self.dburl = "host=" + hostname + " port=" + str(port) + \
                     " dbname=" + dbname + " user=" + username + \
                     " password=" + password

    # This method is used to actually issue query sql to database. 
    def execute(self, query, autocommit=True):
        with connect(self.dburl) as conn:
            if v.SHOW_SQL:
                print(query.as_string(conn))
            conn.autocommit = autocommit
            with conn.cursor() as cur:
                cur.execute(query)
                if not autocommit:
                    conn.commit()
                try:
                    return cur.fetchall()
                except ProgrammingError as e:
                    return None

    # For mainly debug, This method is used to show sql to be issued to database. 
    def show_sql(self, query):
        with connect(self.dburl) as conn:
            print(query.as_string(conn))

    # search item data
    def search_items(self):
        query = sql.SQL("""
            SELECT * FROM \"items\"
        """)
        # self.show_sql(query)
        results = self.execute(query, autocommit=True)
        item_list = []
        for r in results:
            item = Item()
            item.id = r[0]
            item.owner_id = r[1]
            item.itemname = r[2]
            item.price = r[3]
            item_list.append(item)
        return item_list

    # search item data by itemname
    def search_items_by_itemname(self, errordetail):
        query = sql.SQL("""
            SELECT * FROM \"items\" WHERE itemname LIKE {errordetail}
        """).format(
            errordetail = sql.Literal(errordetail)
        )
        # self.show_sql(query)
        results = self.execute(query, autocommit=True)
        item_list = []
        for r in results:
            item = Error()
            item.errorcode = r[0]
            item.errordetail = r[1]
            item.fixedcode = r[2]
            item.solve = r[3]
            item.keyword = r[4]
            item_list.append(item)
        return item_list

    def add_item(self, item):
        query = sql.SQL("""
            INSERT INTO \"items\" ( {fields} ) VALUES ( {values} )
        """).format(
            tablename = sql.Identifier("items"),
            fields = sql.SQL(", ").join([
                sql.Identifier("owner_id"),
                sql.Identifier("itemname"),
                sql.Identifier("price")
            ]),
            values = sql.SQL(", ").join([
                sql.Literal(item.owner_id),
                sql.Literal(item.itemname),
                sql.Literal(item.price)
            ])
        )
        self.execute(query, autocommit=True)
