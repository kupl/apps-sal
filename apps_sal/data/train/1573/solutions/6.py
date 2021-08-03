try:
    for _ in range(int(input())):
        n = int(input())
        if n % 2 == 0:
            print("NO")
        else:
            z = int(((n - 1) / 2))
            print("YES")
            for i in range(n):
                cnt = 0
                N = []
                while cnt < z:
                    N.append((i + 1 + cnt) % n)
                    cnt += 1
                for j in range(n):
                    if j in N:
                        print(1, end="")
                    else:
                        print(0, end="")
                print()

except EOFError:
    pass
