def max_number(n):
    newlist = str(n)
    lastlist =  "".join(sorted(newlist))[::-1]
    return int(lastlist)
max_number(566797)
