
"""
def num_of_open_lockers(n):
    doors = [0 for i in range(n)]
    for d in range(n):
        for i in range(d, n, d + 1):
            doors[i] = 0 if doors[i] else 1
    return sum(doors)
"""


#  ...  a-ha, OK, gotcha:


def num_of_open_lockers(n): return int(n ** .5)
