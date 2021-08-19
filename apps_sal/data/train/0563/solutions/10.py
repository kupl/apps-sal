for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    for _ in range(int(input())):
        (start, end) = map(int, input().split())
        print(sum(arr[start - 1:end]))
