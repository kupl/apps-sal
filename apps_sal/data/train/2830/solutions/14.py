def db_sort(arr):
    a = list('!' * arr.count('!')) if '!' in arr else []
    return sorted([x for x in arr if isinstance(x, int)]) + a + list(map(str, sorted(map(int, ([x for x in arr if isinstance(x, str) and x[0] in '0123456789']))))) + sorted([x for x in arr if isinstance(x, str) and x[0] not in '0123456789!'])
