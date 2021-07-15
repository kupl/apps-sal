def solve(eq):
    r=[]
    n=""
    for i in eq:
        if i in "*/-+":
            r.append(n)
            r.append(i)
            n=""
        else:
            n+=i
    r.append(n)
    r.reverse()
    return "".join(r)

