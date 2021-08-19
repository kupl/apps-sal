from functools import lru_cache


def strong_num(number):

    @lru_cache()
    def factorial(n):
        if n <= 1:
            return 1
        else:
            print(n)
            return factorial(n - 1) * n
    return 'STRONG!!!!' if sum((factorial(int(x)) for x in str(number))) == number else 'Not Strong !!'
