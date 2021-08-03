def bits_war(n): return (lambda s: "evens win" if s > 0 else "odds win" if s else "tie")(sum(bin(d)[2:].count("1") * (-1)**((d % 2 or d < 0) - (d % 2 and d < 0)) for d in n))
