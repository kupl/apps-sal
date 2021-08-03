import re


def player_manager(players):
    manager = []
    if players:
        players_list = re.findall(r"(?P<name>[a-zA-Z ]+), (?P<number>[0-9]+)", players)

        for name, number in players_list:
            manager.append({'player': name.strip(), 'contact': int(number)})
    return manager
