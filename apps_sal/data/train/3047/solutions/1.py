def repeating_fractions(n, d): return __import__('re').sub(r"(\d)(\1+)(?!\.)", r"(\1)", str(n / float(d)))
