to_binary = lambda n: bin(n + 4294967296 * (n < 0))[2:]
