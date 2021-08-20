def super_size(n):
    n1 = [int(i) for i in list(str(n))]
    n1.sort(reverse=True)
    n1 = int(''.join([str(i) for i in n1]))
    return n1
