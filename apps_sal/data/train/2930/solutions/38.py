# def summation(num):
#     suma = 0
#     if num == 1:
#         return 1
#     else:
#         for x in (1, num+1):
#             suma = suma + summation(x)
#     return suma


def summation(num):
    return sum(range(num + 1))
