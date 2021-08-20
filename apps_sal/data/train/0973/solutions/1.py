t = int(input())
for i in range(t):
    (n, k) = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    print(abs(min(lst) - k) + (max(lst) + k))
