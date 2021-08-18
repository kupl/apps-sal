x = int(input())
for i in range(x):
    (a, b, c) = list(map(int, input().split(' ')))
    if((a + b + c) == 180):
        print("YES")
    else:
        print("NO")
