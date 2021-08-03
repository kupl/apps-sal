ans = []
for i in range(int(input())):
    n, r, x, y = list(map(int, input().split()))
    n = list(range(1, n + 1))
    if x > 0:
        x = list(map(int, input().split()))
    else:
        x = []
    if y > 0:
        x += list(map(int, input().split()))
    x = list(set(x))
    ans.append(min(len(n) - len(x), r))
for i in ans:
    print(i)
