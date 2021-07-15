def table_game(table):
    (a, ab, b), (ac, abcd, bd), (c, cd, d) = table
    if (a + b == ab) and (c + d == cd) and (a + c == ac) and (b + d == bd) and (a + b + c + d == abcd):
        return [a, b, c, d]
    return [-1]
