for _ in range(int(input())):
    n = int(input())
    ls = list(map(int, input().split()))
    ls = sorted(ls)

    print(ls[-2] * ls[-1], end=" ")

    print(ls[0] * ls[1])
