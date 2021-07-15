def cut_the_ropes(a):
    result = []
    while a:
        result.append(len(a))
        m = min(a)
        a = [x-m for x in a if x > m]
    return result
