def build_a_wall(x=0, y=0):
    if not x or not y or type(x) != int or (type(y) != int) or (x < 0) or (y < 0):
        return
    if x * y > 10000:
        return "Naah, too much...here's my resignation."
    (brick, half) = ('■■', '■')
    (m, s) = ('|'.join([brick] * y), half + '|' + '|'.join([brick] * (y - 1)) + '|' + half)
    return '\n'.join([[m, s][i & 1 == x & 1] for i in range(x)])
