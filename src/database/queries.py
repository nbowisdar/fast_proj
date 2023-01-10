from src.database.tablse import Game, Server
from src.schema import Info


def save_in_db(info: Info):
    game = Game.get_or_create(name=info.game_name)[0]
    Server.get_or_create(name=info.server_name, ip=info.ip, game_port=info.game_port,
                         query_port=info.query_port, game=game.id)


def get_all_servers() -> list[Server]:
    pass



if __name__ == '__main__':
    game = Game.select()[0]
    print(game.servers)