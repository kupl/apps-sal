def check(S):
    size = len(S)
    if S[0]=="0" or S[-1]=="1":
        return False
    else:
        for i in range(size-1):
            a, b = i, size-i-2
            if (S[a]=="1" and S[b]=="0") or (S[a]=="0" and S[b]=="1"):
                return False
        return True


S = input()
if check(S):
    N = len(S)
    l = [1]
    p = False
    for i in range(2, N+1):
        if p:
            l.append(i)
        else:
            print((l[-1], i))
        p = (S[i-1]=="1")
    for i in range(len(l)-1):
        print((l[i], l[i+1]))
else:
    print((-1))

