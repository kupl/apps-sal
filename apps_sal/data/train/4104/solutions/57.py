def max_tri_sum(numbers):
    s = []
    for i in numbers:
        if i not in s:
            s.append(i)
    a = sorted(s)[-1]
    b = sorted(s)[-2]
    c = sorted(s)[-3]

    return a + b + c
