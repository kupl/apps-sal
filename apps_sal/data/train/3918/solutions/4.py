def baby_count(x):
    x = x.lower()
    nb = min(x.count('a'), x.count('y'), x.count('b')//2)
    return nb if nb else "Where's the baby?!"
