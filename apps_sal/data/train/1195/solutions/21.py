# cook your dish here
for t in range(int(input())):
    n, a, b, c, d, p, q, y = map(int, input().split())
    l = list(map(int, input().split()))
    foot = (abs(l[b - 1] - l[a - 1])) * p
    train = 0
    if (abs(l[c - 1] - l[a - 1])) * p > y:
        print(int(foot))
        continue
    else:
        train += y + ((abs(l[d - 1] - l[c - 1])) * q) + (abs(l[b - 1] - l[d - 1])) * p
    if train < foot:
        print(int(train))
    else:
        print(int(foot))
