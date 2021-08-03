def to_binary(n): return bin(n + 4294967296 * (n < 0))[2:]
