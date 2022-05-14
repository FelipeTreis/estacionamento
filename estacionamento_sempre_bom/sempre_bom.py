import psycopg2 as db


class Config:
    def __init__(self):
        self.config = {
            "postgres": {
                "user": "postgres",
                "password": "postgres",
                "host": "127.0.0.1",
                "port": "5433",
                "database": "postgres"
            }
        }


class Connection(Config):
    def __init__(self):
        Config.__init__(self)
        try:
            self.conn = db.connect(**self.config["postgres"])
            self.cur = self.conn.cursor()
        except Exception as e:
            print("Erro na conexão", e)
            exit(1)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.connection.close()

    @property
    def connection(self):
        return self.conn

    @property
    def cursor(self):
        return self.cur

    def commit(self):
        self.connection.commit()

    def fetchall(self):
        return self.cursor.fetchall()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())
    
    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()
    

class Estacionamento(Connection):
    def __init__(self):
        Connection.__init__(self)

    def insert(self, *args):
        try:
            sql = "INSERT INTO estacionamento (veiculo, tempo, valor) VALUES (%s, %s, %s)"
            self.execute(sql, args)
            self.commit()
            print("Registro inserido")
        except Exception as e:
            print("Erro ao inserir dados", e)

    def delete(self, veiculo):
        try:
            sql_s = f"SELECT * FROM estacionamento WHERE veiculo = {veiculo}"
            if not self.query(sql_s):
                return "Registro não encontrado"
            sql_d = f"DELETE FROM estacionamento WHERE veiculo = {veiculo}"
            self.execute(sql_d)
            self.commit()
            return "Registro deletado"
        except Exception as e:
            print("Erro ao deletar", e)

    def search(self, *args, type_s="veiculo"):
        sql = "SELECT * FROM estacionamento WHERE veiculo LIKE %s"
        data = self.query(sql, args)
        if data:
            return data
        return "Registro não existente"    