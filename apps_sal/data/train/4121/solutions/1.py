def fight_resolve(d, a):
    return -1 if d.islower() == a.islower() else d if f"{d}{a}".lower() in "aspka" else a
