def find_value(index, last):
    if last < 2:
        return index
    if index > last // 2:
        new_last = last // 2
        new_index = new_last - (last - index)
        return find_value(new_index, new_last) * 2 + 1
    else:
        new_last = last // 2
        new_index = index
        return find_value(new_index, new_last) * 2


def find_value_at_index(p, idx):
    last = (1 << p) - 1
    assert(idx <= last)
    return find_value(idx, last)


T = int(input())
for x in range(T):
    p, i = [int(x) for x in input().split()]
    print(find_value_at_index(p, i))
