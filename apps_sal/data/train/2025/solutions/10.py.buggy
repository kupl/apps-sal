prime = [2, 3, 5, 7, 11, 13]


def create_list(n):
    nonlocal prime
    for x in range(15, n + 1, 2):
        notPrime = False
        hold = int(x**0.5) + 1
        for j in prime:
            if j > hold:
                break
            if x % j == 0:
                notPrime = True
                break
        if notPrime == False:
            prime.append(x)


def main():
    nonlocal prime
    mode = "filee"
    if mode == "file":
        f = open("test.txt", "r")
    if mode == "file":
        n = int(f.readline())
    else:
        n = int(input())
    create_list(n)
    k = []
    for j in range(len(prime)):
        num = prime[j]
        while num <= n:
            k.append(num)
            num *= prime[j]
        j += 1
    print(len(k))
    for i in k:
        print(i, end=' ')
    if mode == "file":
        f.close()


def __starting_point():
    main()


__starting_point()
