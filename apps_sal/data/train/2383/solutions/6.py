for case in range(int(input())):
    (a, b) = [int(x) for x in input().split()]
    print(max(max(a, b), 2 * min(a, b)) ** 2)
