def scoring(array):
    res = {}

    for e in array:
        score = e["norm_kill"] * 100 + e["assist"] * 50 + e["damage"] // 2 +\
            e["healing"] + 2 ** e["streak"] + e["env_kill"] * 500

        res[e["name"]] = score

    return sorted(res, key=res.get, reverse=True)
