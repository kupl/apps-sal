# cook your dish here

T = int(input())

for _ in range(T):

    n = int(input())
    x = list(map(int, input().split()))

    print(min(x) * (n - 1))
