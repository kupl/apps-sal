def boredom(staff):
    scores = {"accounts" : 1, "finance" : 2, "canteen" : 10,
              "regulation" : 3, "trading" : 6, "change" : 6,
              "IS" : 8, "retail" : 5, "cleaning" : 4, "pissing about" : 25}
    score = sum(scores[team] for team in staff.values())
    return "kill me now" if score <= 80 else "party time!!" if score >= 100 else "i can handle this"
