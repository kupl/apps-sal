final_attack_value = f = lambda x, m: m and f(x + __import__('fractions').gcd(min(m[0], x), m[0]), m[1:]) or x
