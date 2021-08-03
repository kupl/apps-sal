for _ in range(int(input())):
    n = input().strip()
    a = [98, 57, 31, 45, 46]
    x = []
    for i in range(len(n)):
        x.append(ord(n[i]) - 65 + a[i])
    for i in x:
        s = i % 26
        print(chr(s + 65), end="")
    print()
