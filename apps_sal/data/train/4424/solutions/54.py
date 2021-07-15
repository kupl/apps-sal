from functools import reduce

def expression_matter(a, b, c):
    return reduce(lambda accum, next : accum * next if accum*next > accum+next else accum + next, [c, b, a] if c < a else [a, b ,c])

