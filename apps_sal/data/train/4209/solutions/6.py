def largest_rect(r):
    s,m = [-1], 0
    for i in range(len(r)):
        while s[-1]!=-1 and r[s[-1]]>=r[i]:m=max(m,r[s.pop()]*(i-s[-1]-1))
        s.append(i)
    while s[-1]!=-1:m=max(m,r[s.pop()]*(len(r)-s[-1]-1))
    return m
