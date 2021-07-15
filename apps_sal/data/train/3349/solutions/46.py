def find_missing_number(s):
    if s == '': return 0
    a = s.split(' ')
    if not all([x.isdigit() for x in a]): 
        return 1
    b = sorted([int(x) for x in a])
    c = list(range(1, b[-1]+1))
    if b == c: 
        return 0
    else: 
        for x in c:
            if x not in b:
                return x
    return "I've missed something"
