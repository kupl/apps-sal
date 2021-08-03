def is_even(n):
    return int(n) % 2 == 0


def split_odd_and_even(n):
    index, s = 0, str(n)
    l = [[s[0]]]
    for x in s[1:]:
        if is_even(x) and is_even(l[index][-1]):
            l[index].append(x)
        elif not is_even(x) and not is_even(l[index][-1]):
            l[index].append(x)
        else:
            l.append([x])
            index += 1
    return [int(''.join(x)) for x in l]
