def duck_shoot(ammo, aim, ducks):
    indices = [i for (i, c) in enumerate(ducks) if c == '2']
    hits = int(aim * ammo)
    result = list(ducks)
    for i in indices[:hits]:
        result[i] = 'X'
    return ''.join(result)
