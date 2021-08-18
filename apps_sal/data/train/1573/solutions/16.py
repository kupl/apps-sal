t = int(input())
for _ in range(t):
    n = int(input())
    a = (n - 1) // 2

    if n % 2 == 0:
        print("NO")
    else:
        print("YES")
        for i in range(n - a):
            print("0" * (i + 1) + "1" * a + "0" * (n - i - 1 - a))
        for i in range(a):
            print("1" * (i + 1) + "0" * (n - a) + "1" * (a - i - 1))
