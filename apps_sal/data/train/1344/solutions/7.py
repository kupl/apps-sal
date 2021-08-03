# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    k = 0
    for i in range(2):
        k += min(s)
        s.remove(min(s))
    print(k)
