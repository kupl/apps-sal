def solved(s): return ''.join(sorted(s[:len(s) // 2] + s[len(s) // 2 + int(len(s) & 1):]))
