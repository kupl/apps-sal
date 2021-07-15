def friend(x):
    enemy = []
    [enemy.append(y) for y in x if len(y) != 4]
    [x.remove(z) for z in enemy]
    return x
