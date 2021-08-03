from math import sqrt


def list_squared(m, n):

    def sum_divisors_squared(n):
        def divisors(n):
            for i in range(1, int(sqrt(n) + 1)):
                if n % i == 0:
                    yield i
                    if i * i != n:
                        yield n / i

        return sum(i ** 2 for i in divisors(n))

    def is_square(n):
        return sqrt(n) % 1 == 0

    def gen_subarrays(m, n):
        for i in range(m, n):
            divisor_sum = sum_divisors_squared(i)
            if is_square(divisor_sum):
                yield [i, divisor_sum]
    return [subarray for subarray in gen_subarrays(m, n)]
