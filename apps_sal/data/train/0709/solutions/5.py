for i in range(int(input())):
    n = input()
    l = list(map(int, input().split()))
    print(max(l[0], l[-1]))
