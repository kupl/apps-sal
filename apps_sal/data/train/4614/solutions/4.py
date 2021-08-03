def scoreboard(who_ate_what):
    weights = {"chickenwings": 5, "hamburgers": 3, "hotdogs": 2}

    def score(dude):
        return sum(weights[key] * amount for key, amount in dude.items() if key != "name")
    return sorted(({"name": dude["name"], "score": score(dude)} for dude in who_ate_what), key=lambda d: (-d["score"], d["name"]))
