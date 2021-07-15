evil = lambda n: ["It's Evil!", "It's Odious!"][bin(n).count("1") & 1]
