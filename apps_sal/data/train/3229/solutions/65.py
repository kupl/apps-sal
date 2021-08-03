# import math
# def am_i_wilson(n):
#     n1 = math.ceil(math.sqrt(n))
#     c = 0
#     if n <= 1:
#         return False
#     for i in range(2, n1 + 1):
#         if n%i == 0:
#             c+= 1
#     if c != 0:
#         return False
#     x = (math.factorial(n-1)+1)/((n**2))

#     return x.is_integer()


# import math

# def am_i_wilson(n):
#     if n <= 2:
#         return False
#     fact=math.factorial(n-1)
#     if (fact+1)%n==0:
#         if (fact+1)%(n**2)==0:
#             return True
#         return False
#     return False

def am_i_wilson(n):
    return n in (5, 13, 563)
