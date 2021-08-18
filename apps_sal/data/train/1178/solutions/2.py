for _ in range(int(input())):
    n = int(input())
    sum = 0
    l = [int(item) for item in input().split()]
    l.sort()
    for i in range(n):
        if l[i] == 0:
            sum = sum + 1
        elif l[i] <= sum:
            sum = sum + 1
    print(sum)
