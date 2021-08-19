def insert_dash2(x):
    return ''.join([str(x)[i] + '-' if int(str(x)[i]) % 2 and int(str(x)[i + 1]) % 2 else str(x)[i] + '*' if not int(str(x)[i]) % 2 and (not int(str(x)[i + 1]) % 2) and ('0' not in [str(x)[i + 1], str(x)[i]]) else str(x)[i] for i in range(len(str(x)) - 1)]) + str(x)[-1]
