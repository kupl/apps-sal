p = lambda b,c=1: [*p(b[:-1],1-b[-1]&c), 1-b[-1]^c] if len(b) else []
positive_to_negative = p
