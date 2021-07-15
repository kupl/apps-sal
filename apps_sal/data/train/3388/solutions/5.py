binary_to_string = lambda b: "".join([[chr(l) for l in range(0, 127)][m] for m in [int(b[n: n+8],2) for n in range(0, len(b), 8)]])
