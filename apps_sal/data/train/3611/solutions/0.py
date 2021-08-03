def ranking(a):
    a.sort(key=lambda x: (-x["points"], x["name"]))
    for i, x in enumerate(a):
        x["position"] = i + 1 if not i or x["points"] < a[i - 1]["points"] else a[i - 1]["position"]
    return a
