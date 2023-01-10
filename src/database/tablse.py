from pathlib import Path
from peewee import SqliteDatabase, Model, CharField, IntegerField, ForeignKeyField

BASE_DIR = Path(__file__).parent.parent.parent
db = SqliteDatabase(BASE_DIR / 'old.db')


class BaseModel(Model):
    class Meta:
        database = db


class Game(BaseModel):
    name = CharField(unique=True)


class Server(BaseModel):
    name = CharField()
    ip = CharField()
    game_port = IntegerField()
    query_port = IntegerField()
    game = ForeignKeyField(ForeignKeyField(Game), backref="servers")


def create_tables():
    tables = [Game, Server]
    db.create_tables(tables)


if __name__ == '__main__':
    create_tables()
