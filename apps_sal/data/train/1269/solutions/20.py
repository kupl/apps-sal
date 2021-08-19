for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    b = sorted(map(int, input().split()))
    print(sum(map(min, list(zip(a, b)))))
