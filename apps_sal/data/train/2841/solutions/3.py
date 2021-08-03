from math import ceil
def char_attribute(n): return (lambda m: {"modifier": n and m, "maximum_spell_level": -1 if n < 10 else min([n - 10, 9]), "extra_spells": [e for e in [(lambda s: s if s > 0 else None)(ceil((m - i) / 4)) for i in range(9)] if e != None]})(n // 2 - 5 if n else -1)
