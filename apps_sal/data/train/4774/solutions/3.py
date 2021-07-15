find_in_array = lambda seq, predicate: (lambda ret: -1 if not ret else ret[0])([i for i, e in enumerate(seq) if predicate(e,i)])
