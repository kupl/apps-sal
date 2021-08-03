def super_size(n):
    # your code here

    s = [int(i) for i in str(n)]
    s.sort(reverse=True)
    s = [str(x) for x in s]
    res = int("".join(s))
    return res
