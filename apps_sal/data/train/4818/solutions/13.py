# find len of str
# if len a > len b
# do bab
# else do aba
def solution(a, b):
    p = len(a)
    w = len(b)
    if p > w:
        l = b + a + b
        return l
    else:
        m = a + b + a
        return m

