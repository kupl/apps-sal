for _ in range(int(input())):
    n = int(input())
    if (n - 1) % 2 != 0:
        print("NO")
    else:
        print("YES")
        b = [0] * n
        for i in range((n - 1) // 2):
            b[i + 1] = 1
        print(*b, sep="")
        for j in range(n - 1, 0, -1):
            print(*(b[j:] + b[:j]), sep="")
