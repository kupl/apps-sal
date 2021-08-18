for i in range(int(input())):
    N = int(input())
    l = list(map(int, input().split()))
    for j in range(int(input())):
        q1, q2 = map(int, input().split())
        temp = l[q1 - 1: q2]
        print(sum(temp))
