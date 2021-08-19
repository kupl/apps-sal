def commas(num):
    i = round(num, 3)
    f = int(i)
    return f'{(f if f == i else i):,}'
