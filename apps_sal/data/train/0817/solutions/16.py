# cook your dish here
tc = int(input())
while tc:
    tc -= 1
    n = int(input())
    lst = list(map(int, input().split()))
    t = 0
    for x in lst:
        t = t^x
    print(t)
