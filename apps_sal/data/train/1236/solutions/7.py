for _ in range(int(input())):
    n = int(input())
    s = input()
    c = 0
    if n == 1:
        print("0")
    else:
        p = s[0]
        for i in range(1, n):
            if p == s[i]:
                c += 1
            p = s[i]
        print(c)
