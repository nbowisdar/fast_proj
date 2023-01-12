from typing import NamedTuple


class Info(NamedTuple):
    server_name: str
    ip: str
    game_port: int
    query_port: int
    game_name: str
    address: str = None
