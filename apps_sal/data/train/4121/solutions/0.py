def fight_resolve(d, a):
    return -1 if d.islower() == a.islower() else d if d.lower() + a.lower() in "ka sp as pk" else a
