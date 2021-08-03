def e_red_scarf():
    from functools import reduce
    N = int(input())
    A = [int(i) for i in input().split()]

    total = reduce(lambda x, y: x ^ y, A)
    ans = [a ^ total for a in A]
    return ' '.join(map(str, ans))


print(e_red_scarf())
