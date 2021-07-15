def simplify(n):
    d = max(m for m in range(1, int(n**0.5)+1) if m*m <= n and n % (m*m) == 0)
    r = n // (d*d)
    return str(d) if r == 1 else "sqrt {}".format(r) if d == 1 else "{} sqrt {}".format(d, r)

def desimplify(s):
    d, r = s.split("sqrt") if "sqrt" in s else (s, "1")
    d = d if d else "1"
    return int(d)*int(d)*int(r)
