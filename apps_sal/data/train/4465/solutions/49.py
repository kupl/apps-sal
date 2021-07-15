def super_size(n):
    uporz = list(str(n))
    uporz.sort(reverse=True)
    return int(''.join(uporz))
