for _ in range(int(input())):
    n = int(input())
    if(n % 2 == 0):
        print("NO")
    else:
        print("YES")
        for i in range(n):
            l = ["0"] * n
            for j in range(i, i + n // 2):

                l[((j + 1) % n)] = "1"
            print("".join(l))
