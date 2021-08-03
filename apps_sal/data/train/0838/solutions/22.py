for _ in range(int(input())):
    input()
    a = list(map(int, input().split()))
    print(max(a[i] + i for i in range(len(a))))
