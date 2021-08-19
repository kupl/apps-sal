def is_prime(n):
    # base cases handling
    if n == 2 or n == 3:
        return True  # handles 2, 3
    if n < 2 or n % 2 == 0:
        return False  # handles 1 and even numbers
    if n < 9:
        return True  # since 1, 2, 3, 4, 6 and 8 are handled, this leaves 5 and 7.
    if n % 3 == 0:
        return False  # handles multiples of 3
    r = int(n**0.5)  # only check upto square root
    f = 5  # start from 5
    while f <= r:
        #print ('\t', f)
        if n % f == 0:
            return False  # essentially checks 6n - 1 for all n.
        if n % (f + 2) == 0:
            return False  # essentially checks 6n + 1 for all n.
        f += 6  # incrementing by 6.
    return True


def max_even_digits_in_prime(n):
    return (len(str(n)) - 1) or 1


def count_of_even_digits(n):
    count = 0
    for i in str(n):
        count += (int(i) % 2 == 0)
    return count


def f(n):
    best_case = (0, 0)  # keeps track of highest best case number seen[1], and its count of even digits[0]
    for x in range(n - 1, 1, -1):  # iterate in the reverse direction
        # print(x)
        if is_prime(x):  # proceed for prime numbers
            even_digits = count_of_even_digits(x)
            max_even_digits = max_even_digits_in_prime(x)
            if best_case[0] < even_digits:  # update best number seen so far
                best_case = (even_digits, x)
            if max_even_digits == best_case[0]:  # best case answer, your work is done. No need to look for more numbers.
                print(best_case)
                return (best_case[1])
