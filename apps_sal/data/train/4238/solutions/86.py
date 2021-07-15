import math

def squares_needed(grains):
    if grains == 0:
        return 0
    return int(math.log2(grains)) + 1
#     for i in range(64):
#         while grains <= (2 ** i):
#             return i

