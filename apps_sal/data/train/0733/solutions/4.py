for _ in range(int(input())):
    n = int(input())
    s = input()
    minn = ord(s[0])
    for i in range(1, n):
        minn = min(ord(s[i]), minn)

    print(chr(minn))
