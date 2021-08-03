def modify(s, i, j):
    k = s[i]
    del(s[i])
    s.insert(j, k)
    return(str(s))


for _ in range(int(input())):
    n = int(input())
    s = list(input())

    ans = str(s)
    for i in range(n):
        for j in range(n):
            if i != j:
                ans = min(ans, modify(s, i, j))
            k = s[j]
            del(s[j])
            s.insert(i, k)

    for i in ans:
        if ord(i) >= 65 and ord(i) <= 90:
            print(i, end="")
    print()
