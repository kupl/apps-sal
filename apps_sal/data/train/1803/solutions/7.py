from itertools import combinations


def funk(*args):
    num = 1
    for i in args[0]:
        num *= i
    num = str(num)
    d_2 = {i: num.count(i) // 2 for i in num if num.count(i) // 2}
    d_1 = {i: num.count(i) % 2 for i in num if num.count(i) % 2}
    main_part = ''.join([d_2[i] * i for i in sorted(d_2, reverse=True)])
    add_part = max(d_1) if d_1 else ''
    res = main_part + add_part + main_part[::-1]
    res = res.strip('0')
    return int(res)


def numeric_palindrome(*args):
    if all([i in [0, 1] for i in args]) and args.count(1) >= 2:
        return 1
    l_new = [i for i in args if i not in [0, 1]]
    l_new = l_new + [1] if 1 in args else l_new
    l = [l_new]
    if len(l_new) < 2:
        return 0
    for i in range(2, len(l_new)):
        l += [tuple_ for tuple_ in combinations(l_new, i)]
    l = [funk(i) for i in l]
    return max(l)
