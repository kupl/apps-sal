def over_the_road(address, n):
#     odd, even = [], []
#     for i in range(1, n*2+1):
#         if i % 2 == 0:
#             even += [i]
#         if i % 2 != 0:
#           odd += [i]
#     even = even[::-1]

#     return even[odd.index(address)] if address in odd else odd[even.index(address)]
    return n*2+1 - address
