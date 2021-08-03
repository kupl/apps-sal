def triple_trouble(one, two, three): return "".join(["".join([x[i] for x in (one, two, three)]) for i in range(len(one))])
