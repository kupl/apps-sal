def max_tri_sum(numbers):
    lst = sorted(numbers[:3])
    for i in numbers[3:]:
        if i > lst[0]:
            if i not in lst:
                for x in range(len(lst)):
                    if i < lst[x]:
                        del lst[0]
                        lst.insert(x - 1, i)
                        break
                    elif i > lst[2]:
                        del lst[0]
                        lst.append(i)
                        break
    return sum(lst)
