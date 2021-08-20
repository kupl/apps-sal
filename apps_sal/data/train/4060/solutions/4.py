from queue import deque


def ant_bridge(ants, terrain):
    terrains = '-' + terrain + '-'
    marching_ants = deque(([ant, -len(ants) + count + 1] for (count, ant) in enumerate(ants)))
    print(marching_ants)
    bridge_ants = deque()
    for pos in range(1, len(terrains) - 1):
        if '.' in terrains[pos - 1:pos + 2]:
            leading_ant = marching_ants.pop()
            leading_ant[1] = pos
            bridge_ants.append(leading_ant)
            march_forward(marching_ants, bridge_ants)
        else:
            march_forward(marching_ants, bridge_ants)
    while len(bridge_ants) > 0:
        march_forward(marching_ants, bridge_ants)
    return ''.join((ant[0] for ant in marching_ants))


def march_forward(marching_ants, bridge_ants):
    """
    将整个行进蚁前移一格，并拆掉最尾端空闲的桥蚁
    :param marching_ants: 行进蚁队列
    :param bridge_ants: 桥蚁队列
    """
    print(marching_ants, bridge_ants)
    for ant in marching_ants:
        ant[1] += 1
    if len(marching_ants) == 0 or (len(bridge_ants) > 0 and bridge_ants[0][1] < marching_ants[0][1]):
        marching_ants.appendleft(bridge_ants.popleft())
