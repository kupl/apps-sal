for _ in range(int(input())):
    n = int(input())
    s = input()
    if(n == 1):
        print("No")
        continue
    f = 0
    p = "AEIOU"
    c = 0
    for i in range(len(s) - 1):
        if(s[i] in p and s[i + 1] in p):
            f += 1
    if(s[0] in p and s[n - 1] in p):
        f += 1
    if(f >= 1):
        print("Yes")
    else:
        print("No")
