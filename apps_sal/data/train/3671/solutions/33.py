def problem(a):
    b = str(a)
    if b.replace('.', '').isdigit():
        return a * 50 + 6
    elif a.isalpha():
        return 'Error'
