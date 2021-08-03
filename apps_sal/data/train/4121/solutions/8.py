def fight_resolve(d, a):
    if d.islower() == a.islower():
        return -1
    map = {"a": "s", "k": "a", "p": "k", "s": "p"}
    return d if map[d.lower()] == a.lower() else a
