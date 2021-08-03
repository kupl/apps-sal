def zeros(n): return n // 5 + zeros(n / 5) if n / 5 else 0
