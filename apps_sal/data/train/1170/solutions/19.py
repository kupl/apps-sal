for _ in range(int(input())):
    n, k = map(int, input().split())
    l = [int(x) for x in input().split()]
    for i in l:
        if(i % k == 0):
            print("1", end="")
        else:
            print("0", end="")
    print()
