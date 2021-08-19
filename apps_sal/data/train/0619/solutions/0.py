n = int(input())
for i in range(n):
    l = list(map(int, input().split()))
    k = l[0] + l[1]
    k = k % (2 * l[2])
    if k >= 0 and k < l[2]:
        print('CHEF')
    else:
        print('COOK')
