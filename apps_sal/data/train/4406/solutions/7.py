tram = lambda s, d, o,a=__import__("itertools").accumulate: max(a(map(int.__sub__, o[:s], d[:s])))
