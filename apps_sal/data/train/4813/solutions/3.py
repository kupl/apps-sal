def get_num(n):
    return sum(([0, [1, 2][i == '8']][i in '0689'] for i in str(n)))
