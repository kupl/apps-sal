# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    p = input()
    if s.count('1') != p.count('1'):
        print("No")
        continue
    c = 0
    ans = True
    for i in range(n):
        if s[i] != p[i]:
            if s[i] == '0':
                if c > 0:
                    c = c - 1
                else:
                    ans = False
                    break
            else:
                c = c + 1
    if ans:
        print("Yes")
    else:
        print("No")
