def scoring(array):
    res = {e["name"]: e["norm_kill"] * 100 + e["assist"] * 50 + e["damage"] // 2 +\
        e["healing"] + 2 ** e["streak"] + e["env_kill"] * 500 for e in array}
    
    return sorted(res, key=res.get, reverse=True)
