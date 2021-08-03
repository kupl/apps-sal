def solve(s):
    slist = list(s)
    revlist = [slist.pop() for _ in range(len(s))]
    revlist[:] = [x for x in revlist if x != ' ']
    slist = list(s)
    for i in range(len(slist)):
        if slist[i] == ' ':
            revlist.insert(i, ' ')
    rev = ''.join(revlist)
    return rev
