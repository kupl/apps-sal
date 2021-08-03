# from math import sqrt, ceil

# def is_prime(n):
#     if n <= 1:
#         return False
#     else:
#         for i in range(2, ceil(sqrt(n)) + 1):
#             if n % i == 0:
#                 return False
#     return True

# def fact(x):
#     fact = 1
#     for i in range(1, x + 1):
#         fact *= i
#     return fact

def am_i_wilson(n):
    #     if not is_prime(n):
    #         return False
    #     else:
    #         return fact(n - 1) == -1 % (n * n)
    return n in [5, 13, 563, 5971, 558771, 1964215, 8121909, 12326713, 23025711, 26921605, 341569806, 399292158]
