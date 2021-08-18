testcases = int(input())
for t in range(testcases):
    n, k = map(int, input().split())
    S = list(map(int, input().split()))
    S.sort(reverse=True)
    count = k
    current = S[k - 1]
    i = k
    while i < n and S[i] == S[k - 1]:
        i += 1
        count += 1
    print(count)
