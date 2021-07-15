from math import floor, ceil

def round_it(n: float) -> int:
    """ Round the given number based on integer / fractal part. """
    _integer_len, _fractal_len = list(map(len, str(n).split(".")))
    round_f = {
        _integer_len < _fractal_len: ceil,
        _integer_len > _fractal_len: floor,
        _integer_len == _fractal_len: round
    }
    return round_f[True](n)
