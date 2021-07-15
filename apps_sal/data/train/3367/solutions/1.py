from math import factorial as f
routes=lambda n:f(n*2) // (f(n)*f(n)) if n>0 else 0
