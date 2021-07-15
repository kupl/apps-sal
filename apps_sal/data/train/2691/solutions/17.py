def solve(s):
    w=''.join(['*' if i.isalpha() else i for i in s])
    num=[int(i) for i in w.split('*') if i]
    return max(num)
