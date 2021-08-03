t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    half = n // 2
    count = 0
    for i in l:
        if(i >= half):
            count += 1
    print(count)
