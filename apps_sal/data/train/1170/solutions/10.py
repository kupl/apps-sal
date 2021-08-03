for _ in range(int(input())):
    x, y = map(int, input().split())
    l = list(map(int, input().split()))
    for i in l:
        if(i % y == 0):
            print("1", end="")
        else:
            print("0", end="")
    print()
