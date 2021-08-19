def permutate(arr):
    if len(arr) == 1:
        yield arr
    for x in range(len(arr)):
        for perm in permutate(arr[:x] + arr[x + 1:]):
            yield ([arr[x]] + perm)


vals = [int(x) for x in input().split()]
founded = False
for val in permutate(vals):
    if val[0] / float(val[1]) == val[2] / float(val[3]):
        print('Possible')
        founded = True
        break
if not founded:
    print('Impossible')
