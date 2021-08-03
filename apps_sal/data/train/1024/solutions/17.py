value = 0
val = int(input())
for i in range(val):
    s, n, a, b = list(map(int, input().split()))
    sum = a
    total = a
    n -= 1
    while(n):
        sum = sum * b
        total += sum
        n -= 1
    if(s >= total):
        print("POSSIBLE ", s - total)
        value += s - total
    else:
        print("IMPOSSIBLE ", total - s)
        value -= total - s
if(value >= 0):
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
