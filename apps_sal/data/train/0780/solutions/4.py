t = int(input())
for i in range(t):
    li = list(map(int, input().split()))
    if li[0] % li[1] % 2 == 0:
        print('EVEN')
    else:
        print('ODD')
