import sqlite3

class ControllerDB:
    def __init__(self):
        self.connector = None
        self.cursor = None
        self.create_connection()

    # Establece la conexión con la base de datos
    def create_connection(self) -> None:
        try:
            self.connector = sqlite3.connect('database/ecuplot_db.db')
            self.cursor = self.connector.cursor()

            print("Conexión creada correctamente")
        except sqlite3.Error as e:
            print(f"Error al conectar con la base de datos: {e}")

    # Se usa la primera vez para crear la tabla
    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS users_telegram (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            imagen BLOB
        );"""

        self.cursor.execute(query)
        self.connector.commit()

        print("Tabla creada correctamente")

    # Retorne el usuario si existe en la tabla
    def get_user_id(self, user_id) -> tuple:
        query = "SELECT * FROM users_telegram WHERE user_id = (?)"

        self.cursor.execute(query, (user_id, ))
        return self.cursor.fetchone()

    # Retorna la imagen del usuario si existe en la tabla
    def get_image_user(self, user_id) -> bytes:
        query = "SELECT imagen FROM users_telegram WHERE user_id = (?)"

        self.cursor.execute(query, (user_id, ))
        return self.cursor.fetchone()[0]

    # Se guarda el usuario en la tabla
    def save_user(self, user_id) -> None:
        query = "INSERT INTO users_telegram (user_id) VALUES (?);"

        self.cursor.execute(query, (user_id, ))
        self.connector.commit()

    # Se actualiza la imagen del usuario en la tabla
    def save_image_user(self, user_id, imagen) -> None:
        if not self.get_user_id(user_id):
            self.save_user(user_id)

        query = "UPDATE users_telegram SET imagen = (?) WHERE user_id = (?)"

        self.cursor.execute(query, (imagen, user_id))
        self.connector.commit()