def scoreboard(who_ate_what):

    new = [{"name": n["name"], "score": n.get("chickenwings", 0) * 5 +
            n.get("hamburgers", 0) * 3 + n.get("hotdogs", 0) * 2} for n in who_ate_what]

    return sorted(new, key=lambda n: (-n["score"], n["name"]))
