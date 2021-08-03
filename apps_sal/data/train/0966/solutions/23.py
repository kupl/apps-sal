t = int(input())
for i in range(t):
    n, u, d = map(int, input().split())
    l = list(map(int, input().split()))
    ind = 0
    c = 0
    for j in range(n - 1):
        if l[j] < l[j + 1]:
            ans = l[j + 1] - l[j]
            if ans <= u:
                ind = j + 1
            else:
                break
        elif l[j] > l[j + 1]:
            ans = l[j] - l[j + 1]
            if ans <= d:
                ind = j + 1
            else:
                if c == 1:
                    break
                else:
                    ind = j + 1
                    c = c + 1
        elif l[j] == l[j + 1]:
            ind = j + 1
            continue
    print(ind + 1)
