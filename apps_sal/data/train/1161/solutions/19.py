for _ in range(int(input())):
    S = list(input())
    for i in range(len(S)):
        if S[i] == "m" and i > 0 and S[i - 1] == "s":
            S[i - 1] = ""
        elif S[i] == "m" and i < len(S) - 1 and S[i + 1] == "s":
            S[i + 1] = ""
    m = S.count("m")
    sn = S.count("s")
    if m > sn:
        print("mongooses")
    elif m < sn:
        print("snakes")
    else:
        print("tie")
