t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    array = list(map(int, input().split()))
    print(max(array) - min(array) + 2 * k)
