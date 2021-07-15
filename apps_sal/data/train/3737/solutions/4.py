def mod(e):
    i, n = e
    return (n**2 if n > 0 else n) * (3 if i % 3 == 0 else 1) * (-1 if i % 5 == 0 else 1)

def calc(lst):
    return sum(map(mod, enumerate(lst, 1)))
    
#   without loop, as asked   
##############################


# there with a comprehension (so a for):
#def calc(lst):
#    return sum((n**2 if n > 0 else n) * (3 if i % 3 == 0 else 1) * (-1 if i % 5 == 0 else 1) for i, n in enumerate(lst, 1))

