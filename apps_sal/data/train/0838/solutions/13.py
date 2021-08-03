def find(arr):
    hello = []
    for i in range(len(arr)):
        hello.append(arr[i] + i)
    return max(hello)


t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    print(find(arr))
