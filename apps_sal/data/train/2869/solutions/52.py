def distinct(seq):
    done = set()
    return [x for x in seq if not (x in done or done.add(x))]
