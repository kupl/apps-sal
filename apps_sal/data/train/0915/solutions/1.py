# cook your dish here
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    s = set(l)
    l1 = list(s)
    print(len(l1))
