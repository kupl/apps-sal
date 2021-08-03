def main():
    x, r, a, b = list(map(int, input().split()))
    num_meets = int(x * abs(a - b) / max(a, b))
    if (x * (a - b)) % max(a, b) == 0:
        num_meets -= 1
    print(num_meets)


t = int(input())
for _ in range(t):
    main()
