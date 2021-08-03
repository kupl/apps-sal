def calculate_age(birth, curr):
    diff = abs(curr - birth)
    age = "%d year%s" % (diff, "s" * bool(diff - 1))
    return "You were born this very year!" if not diff else "You are %s old." % age if curr > birth else "You will be born in %s." % age
