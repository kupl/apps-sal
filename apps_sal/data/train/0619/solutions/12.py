# cook your dish here
T = int(input())
for _ in range(T):
    p1, p2, k = map(int, input().split())
    num = p1 + p2
    res = num // k
    if res % 2:
        print('COOK')
    else:
        print('CHEF')
