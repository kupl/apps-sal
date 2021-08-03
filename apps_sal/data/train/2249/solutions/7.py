def main():
    # n = int(input())
    # arr = list(map(int, input().split()))
    x1, y1, x2, y2 = list(map(int, input().split()))
    # s = input()
    if x1 == x2 or y1 == y2:
        print(abs(x1 - x2) + abs(y1 - y2))
    else:
        print(abs(x1 - x2) + abs(y1 - y2) + 2)


# for _ in range(1):
for _ in range(int(input())):
    main()
