def primes_upto(limit):
    num_list = [1 for i in range(0, limit + 1)]
    ctr = 2
    is_prime = [True] * (limit + 1)
    for n in range(2, int(limit ** 0.5) + 1):
        if is_prime[n]:
            for i in range(n * n, limit + 1, n):
                is_prime[i] = False
                num_list[i] = ctr
    del num_list[0]
    del num_list[1]
    return num_list


def main():
    jewels = int(input())
    result = primes_upto(jewels + 1)
    print(len(set(result)))
    for i in result:
        print(i, end=' ')


def __starting_point():
    main()


__starting_point()
