t = int(input())
for i in range(t):
    a = int(input())
    a1 = list(map(int, input().split()))[:a]
    x = []
    y = [1, 2, 3, 4, 5, 6, 7]
    z = a1[::-1]
    for i in a1:
        if i not in x:
            x.append(i)
    if(x == y and a1 == z):
        print('yes')
    else:
        print('no')
