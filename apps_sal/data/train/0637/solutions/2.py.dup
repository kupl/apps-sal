

a = int(input())
while a != 0:
    b, c = map(int, input().split())
    p = c - 2
    if p == 0 or p == 2 or b == c:
        print(-1)
    else:
        q = b // p
        r = b % p
        k = 0

        if p + r == c:
            print("(", end="")
            while k != q:

                for i in range(1, p + 1):

                    if i <= (p) // 2:
                        print("(", end="")
                    else:
                        print(")", end="")
                k += 1

            print(")")

            a -= 1
            print()
            continue

        while k != q:

            for i in range(1, p + 1):

                if i <= p // 2:
                    print("(", end="")
                else:
                    print(")", end="")
            k += 1
        for i in range(1, r + 1):
            if i <= r // 2:
                print("(", end="")
            else:
                print(")", end="")

        print()

    a -= 1
