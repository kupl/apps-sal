def super_size(n):
    list = [str(i) for i in str(n)]
    list.sort(reverse=True)
    result = int(''.join(list))
    return result
