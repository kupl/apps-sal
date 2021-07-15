n = int(input())
if n <= 2:
    print(1)
    for i in range(n):
        print(1, end=' ')
else:
    prime = [1] * (n + 2)
    for i in range(2, n + 2):
        if prime[i]:
            k = i
            while k + i < n + 2:
                k += i
                prime[k] = 0
    print(2)
    for i in range(2, n + 2):
        if prime[i]:
            print(1, end=' ')
        else:
            print(2, end=' ')
