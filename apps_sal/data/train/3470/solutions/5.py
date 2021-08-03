def to_twos_complement(s, l): return int(s.replace(' ', ''), 2)if s[0] == '0'else-(int("".join([str(int(i) ^ 1)for i in s.replace(' ', '')]), 2) + 1)
def from_twos_complement(n, b): return bin(n & 0xffffffffffffffffffff)[2:][-b:]if n < 0else bin(n)[2:].zfill(b)
