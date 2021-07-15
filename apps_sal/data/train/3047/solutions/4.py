import re
def repeating_fractions(n,d):
    ok = str((n+0.0)/d).split(".")
    return ok[0]+"."+re.sub(r"(\d)\1+", r"(\1)", ok[1])
