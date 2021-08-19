import re


def player_manager(players):
    return players and [{'player': who, 'contact': int(num)} for (who, num) in re.findall('(.+?), (\\d+)(?:, )?', players)] or []
