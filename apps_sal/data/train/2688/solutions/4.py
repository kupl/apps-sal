def f(n):
    return sum(int(x) ** 2 for x in str(n))
    
def repeat_sequence_len(n):
    d, i = {}, 0
    while n not in d:
        d[n] = i
        i += 1
        n = f(n)
    return i - d[n]
