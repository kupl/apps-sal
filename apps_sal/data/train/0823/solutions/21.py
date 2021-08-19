from itertools import permutations


def check_0(arr):
    if sum(arr) == 0:
        return 'Yes'
    arr_len = len(arr)
    for perm in permutations(arr):
        for j in range(1, arr_len):
            if sum(perm[:j]) == 0:
                return 'Yes'
    return 'No'


for i in range(int(input())):
    arr = [int(x) for x in input().split()]
    print(check_0(arr))
