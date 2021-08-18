from bisect import bisect_left

m = int(input())
lines = []
for i in range(m):
    lines.append(list(map(int, input().split())))
n = int(input())
lengths = list(map(int, input().split()))

sizes = [0]
for l in lines:
    sizes.append(sizes[-1] + (1 if l[0] == 1 else l[1] * l[2]))

result = {}


def find_number(l):
    if l in result:
        return result[l]
    i = bisect_left(sizes, l) - 1
    if lines[i][0] == 1:
        result[l] = lines[i][1]
        return result[l]
    new_l = (l - sizes[i] - 1) % lines[i][1] + 1
    result[new_l] = find_number(new_l)
    return result[new_l]


print(' '.join([str(find_number(l)) for l in lengths]))
