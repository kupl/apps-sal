for _ in range(int(input())):
    s = input()
    a = [int(s[i]) - 2 for i in range(len(s))]
    for i in range(len(s)):
        print(a[i], end='')
    print()
