def how_many_bees(hive):
    return sum(word.count("eeb") + word.count("bee") for word in list(map(lambda x: "".join(list(x)), zip(*hive))) + list(map(lambda x: "".join(x), hive))) if hive else 0
