def problem(a):
    try:
        int(a)
        a *= 50
        a += 6
        return a
    except:
        return 'Error'
