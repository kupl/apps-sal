encode=lambda s: "".join(f"{len(list(group))}{char}" for char, group in __import__("itertools").groupby(s)) 
decode=lambda s: "".join(c * int(n) for n, c in __import__("re").findall(r"(\d+)(\D{1})", s))

