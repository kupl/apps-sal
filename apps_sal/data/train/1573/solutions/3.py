t = int(input())
for i in range(t):
    n = int(input())
    if (n % 2 == 0 or n == 1):
        print("NO")
        continue
    else:
        print("YES")
        p = int((n - 1) / 2)
        for j in range(n):
            c = p + j - n + 1
            for k in range(n):
                if ((j + p) >= n and c >= 1):
                    print("1", end="")
                    c = c - 1
                elif (k >= (j + 1) and k <= (j + p)):
                    print("1", end="")
                else:
                    print("0", end="")
            print("\n", end="")
