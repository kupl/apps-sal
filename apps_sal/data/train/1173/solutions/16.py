# cook your dish here
test_cases = int(input())
for test in range(test_cases):
    n = int(input())
    seq = list(map(int, input().split()))

    triplets = 0
    res = [0 for _ in range(n)]
    for i in range(n - 1):
        res[i] = seq[i]
        for j in range(i + 1, n):
            res[j] = res[j - 1] ^ seq[j]
            if res[j] == 0:
                triplets += (j - i)
    print(triplets)
