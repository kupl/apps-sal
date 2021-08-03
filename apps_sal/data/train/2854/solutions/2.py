def lastname(name):
    name = name.split()
    return name[1]


def sort_reindeer(reindeer_names):
    reindeer_names.sort(key=lastname)
    return reindeer_names
