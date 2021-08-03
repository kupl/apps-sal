import sys
opened = set()
first = True
for line in sys.stdin:
    if first:
        first = False
        continue

    tok = line.split()
    if len(tok) == 1:
        opened = set()
    else:
        x = int(tok[1])
        if x in opened:
            opened.remove(x)
        else:
            opened.add(x)

    print(len(opened))
