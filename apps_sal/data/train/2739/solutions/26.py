def cube_odd(a):
    total = 0
    try:
        for i in a:
            if str(i) is 'False' or str(i) is 'True':
                return None
            total += i ** 3 if i ** 3 % 2 != 0 else 0
        return total
    except:
        return None
