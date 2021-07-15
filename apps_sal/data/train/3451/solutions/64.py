import itertools

LOOKUP = {}
def slow_lookup(x,y):
    if x == y:
        return x
    rem = (set("RGB") - {x,y})
    print(x, y, rem)
    return rem.pop()
for x in "RGB":
    for y in "RGB":
        LOOKUP[x+y] = slow_lookup(x,y)
fast_lookup = lambda x, y: LOOKUP(x+y)
    
def triangle(row):
    print(row)
    for _ in range(len(row)-1):
        row = "".join(LOOKUP[row[x:x+2]] for x in range(len(row)-1))
        print(row)
    return next(iter(row))
