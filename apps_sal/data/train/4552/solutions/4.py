def rankings(arr):
    ranks = {x: i for i, x in enumerate(sorted(arr, reverse=True), 1)}
    return [ranks[x] for x in arr]
