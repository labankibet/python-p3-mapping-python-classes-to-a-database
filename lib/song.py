from config import CONN, CURSOR

class Song:
    def __init__(self, name, album, id=None):
        self.id = id
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """
        CURSOR.execute(sql)

    def save(self):
        if self.id is None:
            sql = """
                INSERT INTO songs (name, album)
                VALUES (?, ?)
            """
            CURSOR.execute(sql, (self.name, self.album))
            self.id = CURSOR.lastrowid
        else:
            sql = """
                UPDATE songs SET name = ?, album = ?
                WHERE id = ?
            """
            CURSOR.execute(sql, (self.name, self.album, self.id))

    @classmethod
    def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song

