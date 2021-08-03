for _ in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    print(max(li[0], li[-1]))
