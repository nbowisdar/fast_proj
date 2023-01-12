from src.database.tablse import Game, Server, BASE_DIR
from src.schema import Info


def save_in_db(info: Info):
    game = Game.get_or_create(name=info.game_name)[0]
    Server.get_or_create(name=info.server_name, ip=info.ip, game_port=info.game_port,
                         query_port=info.query_port, game=game.id, address=info.address)


def get_all_servers() -> list[Server]:
    pass


def save_to_txt(game_name: str, servers: list[Server], with_adress = False):
    # with open( BASE_DIR / f'results/{game_name}.txt', 'w', encoding='utf-8') as file:
    with open( BASE_DIR / f'results/{game_name}.txt', 'w', encoding='utf-8') as file:
        for server in servers:
            file.write(f"Назва - {server.name}\n")
            file.write(f"ip - {server.ip}:{server.game_port}:{server.query_port}\n")
            if with_adress:
                file.write(f"Домен - {server.address}:{server.game_port}:{server.query_port}\n")
            file.write("\n")


def save_all():
    for game in Game.select():
        servers = Server.select().where(Server.game == game)
        save_to_txt(game.name, servers, with_adress=True)
        print(f'Saved -> {game.name}')


if __name__ == '__main__':
    # game = Game.get(name="btw")
    # servers = Server.select().where(Server.game == game)
    # save_to_txt(game.name, servers)
    save_all()