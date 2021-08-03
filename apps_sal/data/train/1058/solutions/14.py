t = int(input())
ans = []
for _ in range(t):
    n = input()
    a = []
    place = 1
    for i in n:
        a.append(str(int(i) - 2))
    a = ''.join(a)
    ans.append(a)
for _ in ans:
    print(_)
