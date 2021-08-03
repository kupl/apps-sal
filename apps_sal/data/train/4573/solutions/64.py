def over_the_road(address, n):
    return 2 * n - address + 1
    #     oe = address%2
#     list1 = [2*(n-2) + oe - 4*i for i in range(n)]
#     return address+list1[(address-oe)/2]

#     my_street = [1 + i*2 for i in range(n)]
#     op_street = [my_street[-1]+1 - i*2 for i in range(n)]
#     if address % 2 == 0:
#         return my_street[op_street.index(address)]
#     else:
#         return op_street[my_street.index(address)]
