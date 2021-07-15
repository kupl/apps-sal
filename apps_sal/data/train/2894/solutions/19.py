def triple_trouble(one, two, three):
    return "".join(map("".join, zip(list(one), list(two), list(three))))
