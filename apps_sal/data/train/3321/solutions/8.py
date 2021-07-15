evil = lambda n: "It's %s!" % ("Evil" if len(list(filter(lambda d: d == '1', list(bin(n))))) % 2 == 0 else "Odious")
