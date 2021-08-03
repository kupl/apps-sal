t = int(input())

while t:
    k = int(input())

    r = k % 25
    k -= r
    q = k // 25

    if r != 0:
        for i in range(r + 97, 96, -1):
            print(chr(i), end="")

    while q:
        for i in range(122, 96, -1):
            print(chr(i), end="")
        q -= 1

    print(end="\n")

    t -= 1
