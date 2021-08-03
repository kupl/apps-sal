# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    max_rating = 0
    arr = list(map(int, input().split()))
    for i in range(1, len(arr)):
        if i < n - 1:
            x = arr[i - 1] + arr[i] + arr[i + 1]
        else:
            x = arr[i - 1] + arr[i] + arr[(i + 1) % n]
        max_rating = max(x, max_rating)
    print(max_rating)
