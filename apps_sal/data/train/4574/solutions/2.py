FULL = "■■"
HALF = "■"
SEP = "|"


def build_a_wall(x=None, y=None):
    if any((not isinstance(item, int) or item < 1) for item in (x, y)):
        return None
    if x * y > 10000:
        return "Naah, too much...here's my resignation."

    base_row = SEP.join([FULL] * (y - 1))
    odd_row = SEP.join([base_row, FULL])
    even_row = SEP.join([HALF, base_row, HALF])

    return "\n".join(odd_row if i % 2 else even_row for i in range(-x, 0))
