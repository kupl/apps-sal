solve = lambda lst: [sum(i == ord(c.lower()) - 97 for i, c in enumerate(s)) for s in lst]
