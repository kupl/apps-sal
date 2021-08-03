def am_i_wilson(n):
    return n in (5, 13, 563)

# def am_i_wilson(n):
#    #Piece of shit instead of code for piece of shit instead of instructions.
#    #It is really hard to imagine even worse exercise than this for 8 kyu.
#    #Extreamly outdated for 2019 it no longer has place in here.
#     return True if n == 5 or n == 13 or n == 563 else False

# def am_i_wilson(n):
#     if n < 2 or not all(n % i for i in range(2, n)):
#         return False

#     import math
#     return (math.factorial(n - 1) + 1) % (n ** 2) == 0
