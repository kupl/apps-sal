def triple_trouble(one, two, three):
    return "".join(lttr1 + lttr2 + lttr3 for lttr1, lttr2, lttr3 in zip(one, two, three))
