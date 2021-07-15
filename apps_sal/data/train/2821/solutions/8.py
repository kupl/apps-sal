H = {'J':'|', '|':'|', '...':'...'}

trim = lambda b: [[H[h] for h in m] for m in b[:-1]] \
                            + [['...'] * len(b[-1])]
