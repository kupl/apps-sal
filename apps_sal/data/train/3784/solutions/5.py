from heapq import nlargest, nsmallest


def sort_transform(lst):
    first_last = ''.join((chr(n) for n in lst[:2] + lst[-2:]))
    small_big = ''.join((chr(n) for n in nsmallest(2, lst) + nlargest(2, lst)[::-1]))
    return f'{first_last}-{small_big}-{small_big[::-1]}-{small_big}'
