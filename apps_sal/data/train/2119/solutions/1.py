input()
array = [int(n) for n in input().split()]
order = [int(n) - 1 for n in input().split()][::-1]
rights = dict()
lefts = dict()
current_max = 0
results = []
for i in order:
    results.append(current_max)
    if i - 1 in rights and i + 1 in lefts:
        segment_sum = rights[i - 1][1] + lefts[i + 1][1] + array[i]
        rights[lefts[i + 1][0]] = [rights[i - 1][0], segment_sum]
        lefts[rights[i - 1][0]] = [lefts[i + 1][0], segment_sum]
        rights.pop(i - 1)
        lefts.pop(i + 1)
    elif i - 1 in rights:
        segment_sum = rights[i - 1][1] + array[i]
        lefts[rights[i - 1][0]] = [i, segment_sum]
        rights[i] = [rights[i - 1][0], segment_sum]
        rights.pop(i - 1)
    elif i + 1 in lefts:
        segment_sum = lefts[i + 1][1] + array[i]
        rights[lefts[i + 1][0]] = [i, segment_sum]
        lefts[i] = [lefts[i + 1][0], segment_sum]
        lefts.pop(i + 1)
    else:
        segment_sum = array[i]
        lefts[i] = [i, segment_sum]
        rights[i] = [i, segment_sum]
    if segment_sum > current_max:
        current_max = segment_sum
print(*results[::-1], sep='\n')
