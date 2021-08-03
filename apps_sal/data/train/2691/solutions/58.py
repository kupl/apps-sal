def solve(s):
    for n in s:
        if n.isnumeric() == False:
            s = s.replace(n, ' ')
    lst = s.split()
    lst = [int(x) for x in lst]
    return max(lst)
