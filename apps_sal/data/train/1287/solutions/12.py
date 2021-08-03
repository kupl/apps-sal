for _ in range(int(input())):
    S = input()
    M = 1000000007
    l = []
    for i in range(len(S)):
        if (S[i] == "a" or S[i] == "e" or S[i] == "i" or S[i] == "o" or S[i] == "u"):
            l.append(1)
        else:
            l.append(0)
    k = "".join(str(x) for x in l)
    N = int(k, 2) % M
    print(N)
