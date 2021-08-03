def sort_reindeer(reindeer_names):
    reindeer_names.sort(key=lambda x: x.split()[-1])
    return reindeer_names
