# cook your dish here
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    r = 0
    for i in range(len(l) // 2):
        r += abs(l[i] - l[len(l) - i - 1])
    print(r)
