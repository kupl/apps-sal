import sys


def solve(ppp):
    section_start = -1
    moved_left_max = 0
    moved_right_max = 0
    prev = True
    for (i, p) in enumerate(ppp, start=1):
        if i == p:
            if prev:
                moved_left_max = 0
                moved_right_max = 0
                section_start = -1
            prev = True
        else:
            if not prev:
                if moved_left_max > i - 1:
                    return False
                moved_left_max = 0
                moved_right_max = 0
                section_start = i
            if section_start == -1:
                section_start = i
            if i > p:
                if section_start > p:
                    return False
                if moved_right_max > p:
                    return False
                moved_right_max = p
            else:
                if moved_left_max > p:
                    return False
                moved_left_max = p
            prev = False
    return True


(n, *ppp) = list(map(int, sys.stdin))
print('Yes' if solve(ppp) else 'No')
