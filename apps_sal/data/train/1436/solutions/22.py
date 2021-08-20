for _ in range(int(input())):
    s = str(input())
    i = 0
    j = len(s) - 1
    f = 0
    while i < j:
        if s[i] != s[j]:
            f = 1
            break
        i += 1
        j -= 1
    if f == 1:
        print(2)
    else:
        print(1)
