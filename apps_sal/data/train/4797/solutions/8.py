def shorter_reverse_longer(a, b): return b + a[::-1] + b if len(a) >= len(b) else a + b[::-1] + a
