from itertools import count


def find_f1_eq_f2(n, k):
    def is_f1(n, k): return max(map(int, str(n))) < k
    def is_f2(n, k): return set(str(n)) == set(map(str, range(0, k)))
    for i in count(n + 1):
        for j in count(1):
            f1, f2 = is_f1(i * j, k), is_f2(i * j, k)
            if f1 ^ f2:
                break
            elif f1 and f2:
                return i
