def super_size(n):
    lis = []
    for i in str(n):
        lis.append(i)
    lis.sort(reverse = True)
    x = int(''.join(lis))
    return x
