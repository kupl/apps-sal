
T = int(input())

for _ in range(T):
    a, b = list(map(int, input().split()))
    print(max(max(a, b), min(a, b) * 2)**2)
