for _ in range(int(input())):
    n, k = map(int, input().split())
    l = []
    ln = list(map(str, input().split()))
    for i in range(k):
        lk = list(map(str, input().split()))
        l = l + lk
    for a in ln:
        if a in l:
            print("YES", end=" ")
        else:
            print("NO", end=" ")
    print()
