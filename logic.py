import sqlite3
from config import DATABASE

class DB_Manager:
    def __init__(self, database):
        self.database = database
        
    def random_movie(self):
        sql = "SELECT original_title FROM movies ORDER BY RANDOM() LIMIT 1"
       
        return self.__select_data(sql)
            
    def __executemany(self, sql, data):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.executemany(sql, data)
            conn.commit()
    
    def __select_data(self, sql, data = tuple()):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute(sql, data)
            return cur.fetchall()
            
if __name__ == '__main__':
    dbmanager = DB_Manager(DATABASE)
    dbmanager.create_tables()