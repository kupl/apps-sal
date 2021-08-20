t = int(input())
while t > 0:
    n = int(input())
    li = list(map(int, input().split(' ')))
    se = list(set(li))
    print(len(se))
    t -= 1
