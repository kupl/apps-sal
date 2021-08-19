for _ in range(int(input())):
    (n, k) = map(int, input().split())
    arr = list(map(int, input().split()))
    stack = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            stack.append(abs(arr[i] + arr[j] - k))
    print(min(stack), stack.count(min(stack)))
