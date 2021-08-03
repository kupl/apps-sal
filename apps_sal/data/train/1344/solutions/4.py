# cook your dish here
try:
    for t in range(int(input())):
        n = int(input())
        a = list(map(int, input().split(' ')))
        small = min(a)
        a.remove(small)
        small1 = min(a)
        print(small + small1)
except:
    pass
