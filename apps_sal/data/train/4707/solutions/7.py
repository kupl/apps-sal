to_bytes = lambda n, d=__import__("itertools").dropwhile: list(d(("0" * 8).__eq__, map("".join, zip(*[iter(bin(n)[2:].zfill(8 * (((len(bin(n)) - 2) // 8) + 1)))] * 8)))) or ["0" * 8]
