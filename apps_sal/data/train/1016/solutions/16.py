t = int(input())
for i in range(t):
    n = int(input())
    count = 0
    for i in range(n):
        a, b = map(int, input().split())
        if(b - a > 5):
            count = count + 1
    print(count)
