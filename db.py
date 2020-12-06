import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            'CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY, title text, genre text, set_design text, cinematography text, music text, dialogue text, plot text, acting text)'
        )
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT title, genre AVG(set_design, cinematography, music, dialogue, plot, acting)")
        rows = self.cur.fetchall()
        return rows

    def insert(self, title, genre, set_design, cinematography, music, dialogue,
               plot, acting:
        self.cur.execute(
            'INSERT INTO movies VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?)',
            (title, genre, set_design, cinematography, music, dialogue, plot,
             acting))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM movies WHERE id=?", (id, ))
        self.conn.commit()

    def update(self, id, title, genre, set_design, cinematography, music,
               dialogue, plot, acting, avg):
        self.cur.execute(
            'UPDATE movies SET title= ?, genre= ?, set_design= ?, cinematography= ?, music= ?, dialogue= ?, plot= ?, acting= ? WHERE id = ?',
            (title, genre, set_design, cinematography, music, dialogue, plot,
             acting id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


db = Database('flixlist.db')
db.insert('test movie 1', 'comedy', '8', '8.3', '7', '9.2', '9', '7.6')
db.insert('test movie 2', 'comedy', '6', '7.3', '9', '9.4', '5', '8.3')
db.insert('test movie 3', 'comedy', '10', '3.3', '8', '8.2', '5', '7.9')
