def min_value(digits):
    b = []
    a = [b.append(i) for i in digits if i not in b]
    b.sort()
    return int(''.join(str(i) for i in b))
