a = int(input())
for i in range(a):
    b = int(input())
    c = list(map(int, input().rstrip().split()))
    if sum(c) % b == 0:
        print('Yes')
    else:
        print('No')
