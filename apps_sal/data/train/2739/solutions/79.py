# def cube_odd(arr):
#     x = 0
#     for x in arr:
#         if x is not int:
#             return None
#         if x ** 3 == 1:
#             return True
#         elif x % 2 != 0:
#             return False
#     res = cube_odd(x)
#     print(res)

def cube_odd(arr):
    if any(type(x) is not int for x in arr):
        return None
    return sum(x ** 3 for x in arr if x % 2 != 0)


# def cube_odd(arr):
#     #your code here - return None if at least a value is not an integer
#     sum_num = ("undefined, None, nil, NULL")
#     sum_num = len()
#     if sum_num == int():
#         return sum_num
#     else:
#         pass
#     return arr(sum_num)
# def cube_odd(arr):
#       if any(type(x) is not int for x in arr):
#           return None

#       return sum(x ** 3 for x in arr if x % 2 != 0)
