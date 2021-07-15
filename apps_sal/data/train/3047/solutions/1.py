repeating_fractions = lambda n,d: __import__('re').sub(r"(\d)(\1+)(?!\.)",r"(\1)",str(n/float(d)))
