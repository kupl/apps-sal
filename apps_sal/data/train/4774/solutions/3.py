def find_in_array(seq, predicate): return (lambda ret: -1 if not ret else ret[0])([i for i, e in enumerate(seq) if predicate(e, i)])
