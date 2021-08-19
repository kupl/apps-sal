test_cases = int(input())
for i in range(test_cases):
    (N, K) = map(int, input().split())
    scores = list(map(int, input().split()))
    scores = sorted(scores)[::-1]
    print(len([i for i in scores if i >= scores[K - 1]]))
