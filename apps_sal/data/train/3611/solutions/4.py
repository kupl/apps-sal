def ranking(people):
    ranked = sorted(people, key=lambda p: (-p["points"], p["name"]))
    scores = [p["points"] for p in ranked]
    for p in ranked:
        p["position"] = 1 + scores.index(p["points"])
    return ranked
