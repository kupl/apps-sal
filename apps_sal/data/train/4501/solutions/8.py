def inside_out(s): return " ".join(x[:l][::-1] + x[l] * n + x[l + n:][::-1]for x in s.split()for l, n in [(len(x) // 2, len(x) % 2)])
