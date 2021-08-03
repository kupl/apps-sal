# cook your dish here
n = int(input())
for _ in range(n):
    arr = list(map(int, input().split()))
    a = [2, 3, 9]
    count = 0
    for i in range(arr[0], arr[-1] + 1):
        if i % 10 in a:
            count += 1
    print(count)
