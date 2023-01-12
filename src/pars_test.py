import requests
from fake_useragent import UserAgent
import time
from src.database.queries import save_in_db
from src.database.tablse import create_tables
from src.schema import Info

agent = UserAgent().random

next_link = str
err_count = 0


def _save_one(server: dict):
    attr = server['attributes']
    server_name = server['relationships']['game']['data']['id']
    save_in_db(Info(
        game_name=server_name,
        ip=attr['ip'],
        game_port=attr['port'],
        address=attr['address'],
        # query_port=attr['portQuery'],
        query_port=attr['port'],
        server_name=attr['name']
    ))


def parse_ten(data: dict) -> next_link:
    for server in data['data']:
        _save_one(server)
    return data['links']['next']


def main():
    count = 0
    url = "https://api.battlemetrics.com/servers"
    # last
    #url = "https://api.battlemetrics.com/servers?page%5Bkey%5D=1%2C5873087&page%5Brel%5D=next&sort=groupRank&fields%5Bserver%5D=rank%2Cname%2Cplayers%2CmaxPlayers%2Caddress%2Cip%2Cport%2Ccountry%2Clocation%2Cdetails%2Cstatus&relations%5Bserver%5D=game%2CserverGroup&include=serverGroup&filter%5Bgame%5D=minecraft&filter%5BgroupLeader%5D=true"
    while True:
        time.sleep(1)
        resp = requests.get(url, headers={"User-Agent": agent})
        try:
            url = parse_ten(resp.json())
            count += 1
        except Exception as err:
            print(err)
            print(resp)
        finally:
            with open("file.txt", 'w') as file:
                file.write(url)
            print(f'count - {count} / pars link: {url}')


if __name__ == '__main__':
    create_tables()
    main()





