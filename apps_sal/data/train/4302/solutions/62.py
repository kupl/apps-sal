def better_than_average(cp, mp):
    cp.append(mp)
    print(cp)
    d = sum(cp) / len(cp)
    if mp >= d:
        return True
    else:
        return False
