def solve(s):
    others = [sum((x.isupper() for x in s)), sum((x.islower() for x in s)), sum((x.isnumeric() for x in s))]
    return others + [len(s) - sum(others)]
