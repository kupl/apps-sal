for _ in range(int(input())):
    inps = input().strip()
    stck = [inps[0]]
    for i in range(1, len(inps)):
        if len(stck) > 0:
            if inps[i] == stck[-1]:
                stck.pop()
            else:
                stck.append(inps[i])
        else:
            stck.append(inps[i])
    print(len(stck))
