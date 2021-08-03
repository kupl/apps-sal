t = int(input())
while(t):
    t -= 1
    n = int(input())
    ls = list(map(int, input().split()))
    k = 0
    for i in range(0, n - 2):
        if ls[i] == ls[i + 1] and ls[i + 1] == ls[i + 2]:
            k = 1
            break
    if k == 1:
        print("Yes")
    else:
        print("No")
