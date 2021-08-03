def men_from_boys(a): return sorted(set(a), key=lambda e: ~(10**3 + e) * (e % 2) or -10**6 + e)
