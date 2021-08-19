from itertools import permutations


def get_all_players(a):
    players_str = ''.join([''.join(day) for day in a])
    return set(list(players_str))


def all_players_play_everyday(a, players):
    for day in a:
        if not set(list(''.join(day))) == players:
            return False
    return True


def check_if_play_twice_together(a, players):
    all_2mers = list(permutations(players, 2))
    for day in a:
        for team in day:
            team_2mers = list(permutations(list(team), 2))
            for t in team_2mers:
                try:
                    all_2mers.remove(t)
                except:
                    return False
    return True


def valid(a):
    players = get_all_players(a)
    if len(players) < 2:
        return False
    if not all_players_play_everyday(a, players):
        return False
    return check_if_play_twice_together(a, players)
