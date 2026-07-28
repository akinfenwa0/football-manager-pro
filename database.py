import sqlite3


class Database:
    def __init__(self, db_name="football.db"):

        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

        self.create_tables()

    # ------------------------
    # Create Tables
    # ------------------------

    def create_tables(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS clubs(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT,

            budget INTEGER,

            points INTEGER
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS players(

            id INTEGER PRIMARY KEY,

            name TEXT,

            position TEXT,

            rating INTEGER,

            age INTEGER,

            nationality TEXT,

            value INTEGER,

            club TEXT
        )
        """)

        self.connection.commit()

    # ------------------------
    # Save Club
    # ------------------------

    def save_club(self, club):

        self.cursor.execute("""

        INSERT INTO clubs(name,budget,points)

        VALUES(?,?,?)

        """,

        (

            club.name,

            club.budget,

            club.points

        ))

        self.connection.commit()

    # ------------------------
    # Save Player
    # ------------------------

    def save_player(self, player, club_name):

        self.cursor.execute("""

        INSERT INTO players

        VALUES(?,?,?,?,?,?,?,?)

        """,

        (

            player.id,

            player.name,

            player.position,

            player.rating,

            player.age,

            player.nationality,

            player.value,

            club_name

        ))

        self.connection.commit()

    # ------------------------
    # Load Players
    # ------------------------

    def load_players(self):

        self.cursor.execute("SELECT * FROM players")

        return self.cursor.fetchall()

    # ------------------------
    # Load Clubs
    # ------------------------

    def load_clubs(self):

        self.cursor.execute("SELECT * FROM clubs")

        return self.cursor.fetchall()

    # ------------------------
    # Delete Player
    # ------------------------

    def delete_player(self, player_id):

        self.cursor.execute(

            "DELETE FROM players WHERE id=?",

            (player_id,)

        )

        self.connection.commit()

    # ------------------------
    # Close Database
    # ------------------------

    def close(self):

        self.connection.close()
