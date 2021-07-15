shorter_reverse_longer = lambda a, b: b+a[::-1]+b if len(a) >= len(b) else a+b[::-1]+a
