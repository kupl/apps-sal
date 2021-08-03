for t in range(int(input())):
    n = int(input())
    i = 1
    count = 0
    while (i * i <= n):
        if (n % i == 0):
            temp = n / i
            if (i == temp):
                count += 1
            else:
                count += 2
        i += 1
    if (count % 2 == 0):
        print("NO")
    else:
        print("YES")
