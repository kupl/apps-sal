def main():

    n = 1000000
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):

        if (prime[p] == True):

            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    s = []
    s.append(0)
    for p in range(1, n + 1):
        if prime[p]:
            s.append(s[p - 1] + (p))
        else:
            s.append(s[p - 1])
    t = int(input())
    for _ in range(t):
        num = int(input())
        print(s[num] % 10)


main()
