lib = {'a':'α', 'b':'β', 'd':'δ', 'e':'ε', 'i':'ι', 'k':'κ', 'n':'η', 'o':'θ', 'p':'ρ', 'r':'π', 't':'τ', 'u':'μ', 'v':'υ', 'w':'ω', 'x':'χ', 'y':'γ'}
gr33k_l33t = lambda s: "".join([lib[c] if c in lib else c for c in s.lower()])
