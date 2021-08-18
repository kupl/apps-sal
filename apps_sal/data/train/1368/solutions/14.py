for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    if(n >= k):
        print("Yes")
    else:
        print("No")
