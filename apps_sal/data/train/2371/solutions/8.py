for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    rising = False
    i = n-1
    for _ in range(2):
        while i > 0:
            if a[i-1] == a[i] or (a[i-1] < a[i]) == rising:
                i -= 1
            else:
                rising = not rising
                break
    print(i)

