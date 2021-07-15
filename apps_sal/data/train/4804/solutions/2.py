def relations(f, p):
    def same(a, b): return a(p[0], f) == b(p[1], f)
    if same(ID, P): return "Daughter"
    elif same(P, ID): return "Mother"
    elif same(GP, ID): return "Grandmother"
    elif same(ID, GP): return "Granddaughter"
    elif same(P, P): return "Sister"
    elif same(P, GP): return "Niece"
    elif same(GP, P): return "Aunt"
    elif same(GP, GP): return "Cousin"

def ID(child, _): return child
def P(child, f): return next((p for p, c in f if c == child), None)
def GP(child, f): return P(P(child, f), f)
