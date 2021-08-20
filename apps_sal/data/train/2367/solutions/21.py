from collections import Counter


def moves_needed_when_there_is_no_repeated_char(st):
    size_st = len(st)
    sloution = 0
    for _ in range(size_st):
        for ind in range(size_st - 1):
            if st[ind] > st[ind + 1]:
                (st[ind], st[ind + 1]) = (st[ind + 1], st[ind])
                sloution += 1
    return sloution % 2


def check_number_of_chars(st1, st2):
    cnt_a = Counter(st1)
    cnt_b = Counter(st2)
    if cnt_a != cnt_b:
        return False
    else:
        return True


def is_equal(st1, st2, number):
    if st1 == st2:
        return True
    if not check_number_of_chars(st1, st2):
        return False
    if len(set(st1)) < len(st1) or len(set(st2)) < len(st2):
        return True
    if moves_needed_when_there_is_no_repeated_char(st1) == moves_needed_when_there_is_no_repeated_char(st2):
        return True
    else:
        return False


for _ in range(int(input())):
    n = int(input())
    a = list(input())
    b = list(input())
    if is_equal(a, b, n):
        print('YES')
    else:
        print('NO')
