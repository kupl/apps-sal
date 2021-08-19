import operator

res = 0


def billboard(name, price=30):
    #      return operator.mul(len(name), price)

    return sum([len(name) for i in range(price)])

#     res = len(name)
#     c = foo(res,name)

#     [c for i in range(price)]
#     return res

# def foo(res,name):
#         res += len(name)
