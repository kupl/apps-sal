def multiple(x):
    return "{}{}".format("" if x % 3 else "Bang", "" if x % 5 else "Boom") or "Miss"
