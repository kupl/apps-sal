t = int(input())
powers = [1]
for _ in range(20):
    powers.append(powers[-1] * 2)
for _ in range(t):
    (n, l, r) = map(int, input().split())
    print(sum(powers[:l]) + (n - l), sum(powers[:r]) + (n - r) * powers[r - 1])
