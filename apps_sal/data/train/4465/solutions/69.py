def super_size(n):
    items = [int(x) for x in str(n)]
    items.sort(reverse=True)
    itemStr = ''.join((str(d) for d in items))
    return int(itemStr)
