for _ in range(int(input())):
    n = int(input())
    prime = [True for __ in range(n + 1)]
    prime[:2] = [False, False]
    total = 0
    for i in range(2, n + 1):
        if prime[i] is True:
            temp = i * 2
            total += i
            while temp <= n:
                prime[temp] = False
                temp += i
    print(str(total)[-1])
