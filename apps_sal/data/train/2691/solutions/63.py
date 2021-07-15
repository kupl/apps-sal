def solve(s):
    n = ''
    ls = []
    for i in s:
        if i.isnumeric():
            n+=i
        else:
            if n !='':
                ls.append(n)
                n = ''
    if n !='':
        ls.append(n)
    return max(map(float,ls))
