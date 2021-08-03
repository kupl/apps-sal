
def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # all other even numbers are not primes
    if not n & 1:
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    return True


def main():
    n = int(input())
    if n == 1:
        print('1\n1')
    elif n == 2:
        print('1\n1 1')
        # //fkdjfk
    else:
        cnt = 1
        ans = []
        for i in range(1, n + 1):
            if isprime(i + 1):
                ans.append(1)
            else:
                ans.append(2)
                cnt = 2
        print(cnt)
        for i in ans:
            print(i, end=' ')
        print('\n')


def __starting_point():
    main()


__starting_point()
