def sort_reindeer(reindeer_names):
    return sorted(reindeer_names, key=lambda n: n.split()[-1])
