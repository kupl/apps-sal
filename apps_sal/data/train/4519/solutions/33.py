def max_number(n):
    num = []
    num_out = ''
    n = str(n)
    for q in range(len(n)):
        num.append(n[q])
    num.sort()
    for w in num:
        num_out = num_out + w
    return int(num_out[::-1])
