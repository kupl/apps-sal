from itertools import cycle


def traffic_lights(road, n):
    light1 = iter(cycle('RRRRRGGGGGO'))
    light2 = iter(cycle('GGGGGORRRRR'))

    traffic, car = [], -1

    for _ in range(n + 1):
        temp, RL, GL = [], next(light1), next(light2)
        for i in range(len(road)):
            temp.append({'R': RL, 'G': GL}.get(road[i], '.'))
        if car < len(temp) - 1 and temp[car + 1] in 'RO':
            car -= 1
        car += 1
        if car < len(temp):
            temp[car] = 'C'
        traffic.append(''.join(temp))
    return traffic
