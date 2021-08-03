for j in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    c = 0
    for i in range(n - 2):
        if(x[i] == x[i + 1] and x[i] == x[i + 2]):
            c = 1
            break
    if(c == 1):
        print("Yes")
    else:
        print("No")
