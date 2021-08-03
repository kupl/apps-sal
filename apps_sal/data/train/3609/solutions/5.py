def is_onion_array(a):
    if a == []:
        return True
    a = [sum(x) for x in zip(a, a[::-1])]
    a.pop(len(a) // 2)
    for element in a:
        if element > 10:
            return False
    return True
