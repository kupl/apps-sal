def solution(a):
    len_a = len(a)
    a = set(a)
    while len(a) > 1:
        max_a = max(a)
        a.remove(max_a)
        a.add(max_a - max(a))
    return a.pop() * len_a

