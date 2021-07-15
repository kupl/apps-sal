from functools import reduce

expression_matter = lambda a, b, c: reduce( lambda accum, next: accum * next if accum*next > accum+next else accum + next, [a, b, c] if c > a else [c, b, a])
