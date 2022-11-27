import sqlite3

class add:

    db_name = 'database.db'

    products = [('teclado',450),('monitor',2000),('raton',150),('CPU',20000),('pad',250),('cable',800),('RAM',1450),('SSD',700),('HDD',1450)]

    def run_query(db_name,query, parameters = ()):
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    for product in products:
        query = 'insert into product values(null,?,?)'
        parameters = (product[0],product[1])
        run_query(db_name,query,parameters)
        
    
    
