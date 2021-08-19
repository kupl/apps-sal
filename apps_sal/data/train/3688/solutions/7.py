def table_game(table):
    ((a, ab, b), (ac, abcd, bd), (c, cd, d)) = table
    return [a, b, c, d] if ab == a + b and ac == a + c and (bd == b + d) and (cd == c + d) and (abcd == ab + cd) else [-1]
