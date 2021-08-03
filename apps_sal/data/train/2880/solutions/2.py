def seven(m, s=0): return (m, s) if m < 100 else seven(m // 10 - 2 * (m % 10), s + 1)
