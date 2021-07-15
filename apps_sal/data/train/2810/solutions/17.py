solve=lambda arr: [sum(ord(l.lower())-97==i for i,l in enumerate(s)) for s in arr]
