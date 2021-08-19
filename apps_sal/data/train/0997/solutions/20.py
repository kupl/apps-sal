import sys
for _ in range(int(input())):
    (n, m) = sys.stdin.readline().split()
    score = []
    for x in range(int(n)):
        score.append(10)
    for x in range(int(m)):
        (i, j, k) = sys.stdin.readline().split()
        i = int(i)
        j = int(j)
        k = int(k)
        for x in range(i - 1, j):
            score[x] = score[x] * int(k)
    print(sum(score) // int(n))
