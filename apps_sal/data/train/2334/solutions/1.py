def main():
    # n = int(input())
    # arr = list(map(int, input().split()))
    # x1, y1, x2, y2 = map(int, input().split())
    s = input()
    arr = []
    for i in range(len(s)):
        if len(arr) != 0 and s[i] == 'B':
            arr.pop()
        else:
            arr.append(s[i])
    print(len(arr))


# for _ in range(1):
for _ in range(int(input())):
    main()

