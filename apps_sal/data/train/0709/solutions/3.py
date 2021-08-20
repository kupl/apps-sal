t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    print(max(arr[0], arr[-1]))
