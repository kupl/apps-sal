well = lambda a, f=__import__("itertools").chain.from_iterable: {0: 'Fail!', 1: 'Publish!', 2: 'Publish!'}.get(sum(str(w).lower() == 'good' for w in f(a)), 'I smell a series!')
