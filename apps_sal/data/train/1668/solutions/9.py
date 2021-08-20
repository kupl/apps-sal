def next_smaller(n):
    list_number = list(map(lambda x: int(x), str(n)))
    center = None
    for i in range(len(list_number) - 1, 0, -1):
        if list_number[i] < list_number[i - 1]:
            center = list_number[i - 1]
            left = list_number[:i - 1]
            right = list_number[i:len(list_number)]
            break
    if center is None:
        return -1
    else:
        right.sort(reverse=True)
        for i in right:
            if i < center:
                right.append(center)
                center = i
                right.remove(i)
                right.sort(reverse=True)
                left.append(center)
                left.extend(right)
                if left[0] == 0:
                    return -1
                return int(''.join((str(n) for n in left)))
