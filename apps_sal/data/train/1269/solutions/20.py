# MOD = 1000000007
for _ in range(int(input())):
    # n,k = map(int,input().split())
    n = int(input())
    a = sorted(map(int, input().split()))
    b = sorted(map(int, input().split()))
    print(sum(map(min, list(zip(a, b)))))
