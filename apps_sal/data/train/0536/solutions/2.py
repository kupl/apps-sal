t = int(input())
for i in range(0, t):
    s = input().split(' ')
    k = list(map(int, s))
    print(k[1] // k[0])
