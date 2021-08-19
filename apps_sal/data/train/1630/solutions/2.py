def gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a


def survivor(zombies):
    if len(zombies) == 0:
        return -1
    zombies.sort()
    if zombies[0] == 1:
        return 0
    zombies_gcd = 0
    for z in zombies:
        zombies_gcd = gcd(z, zombies_gcd)
    if zombies_gcd != 1:
        return -1
    length = zombies[-1] + 1
    who_is_bitten = [False for i in range(length)]
    for z in zombies:
        who_is_bitten[z] = True
    i = zombies[0] - 1
    consecutive_zombies = 0
    while consecutive_zombies < zombies[0]:
        if not who_is_bitten[i]:
            result = i
            consecutive_zombies = 0
        else:
            consecutive_zombies += 1
            while i + zombies[-1] >= len(who_is_bitten):
                who_is_bitten.append(False)
            for z in zombies:
                who_is_bitten[i + z] = True
        i += 1
    return result
