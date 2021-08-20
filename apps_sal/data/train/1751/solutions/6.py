from collections import deque


def play_round(dist, army_map):
    armies = list(army_map.keys())
    in_flight = {i: list() for i in armies}
    fires_at = {src: dst for (src, dst) in zip(armies, armies[1:] + [armies[0]])}
    while True:
        in_flight = {i: [(travel - speed, speed) for (travel, speed) in bullets] for (i, bullets) in list(in_flight.items())}
        for (i, bullets) in list(in_flight.items()):
            if any((travel <= 0 for (travel, _) in bullets)):
                in_flight[i] = [(travel, speed) for (travel, speed) in bullets if travel > 0]
                army_map[fires_at[i]][0] = (None, None)
        for (i, army) in list(army_map.items()):
            (j, head) = army.popleft()
            if head is not None:
                in_flight[i].append((dist, head))
                army.append((j, head))
        if any((len(army) == 0 for army in list(army_map.values()))):
            return {i: army for (i, army) in list(army_map.items()) if len(army) != 0}


def queue_battle(dist, *armies):
    army_map = {i: deque(enumerate(army)) for (i, army) in enumerate(armies)}
    while len(army_map) >= 2:
        army_map = play_round(dist, army_map)
    if len(army_map) == 0:
        return (-1, tuple())
    (i, army) = list(army_map.items())[0]
    return (i, tuple((j for (j, _) in army)))
