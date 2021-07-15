def sort_reindeer(reindeer_names):
    return sorted(reindeer_names, key=lambda el: el.split(' ')[-1])
