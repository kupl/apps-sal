def simplify(n, m=0):
    return '' if not n else f'{["","+"][m]}{str(n)}' if n < 10 else f'{["","+"][m]}{str(n)[0]}*1{"0"*(len(str(n))-1)}' + simplify(int(str(n)[1:]), 1)
