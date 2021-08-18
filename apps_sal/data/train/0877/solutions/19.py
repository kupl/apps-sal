t = int(input())
for i in range(t):
    x, y, k, n = list(map(int, input().split()))
    val = abs(x - y)
    if(val % k == 0):
        if((val / k) % 2 == 0):
            print("Yes")
        else:
            print("No")
    else:
        print("No")
