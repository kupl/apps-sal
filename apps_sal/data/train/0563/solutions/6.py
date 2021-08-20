t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    q = int(input())
    for j in range(q):
        (q1, q2) = list(map(int, input().split()))
        sum = 0
        for k in range(q1 - 1, q2):
            sum += lst[k]
        print(sum)
