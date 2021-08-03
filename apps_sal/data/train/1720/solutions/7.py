from functools import reduce


class RomanNumerals:

    _map = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
            50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

    @classmethod
    def to_roman(cls, n):
        _map = cls._map
        def red(s, e): return (s[0] + _map[e] * (s[1] // e), s[1] - e * (s[1] // e))
        return reduce(red, reversed(sorted(_map)), ['', n])[0]

    @classmethod
    def from_roman(cls, s):
        _map = {v: k for k, v in cls._map.items()}
        def red(s, e): return s[:-1] + [s[-1] + e] if s and s[-1] + e in _map else s + [e]
        return sum(_map[x] for x in reduce(red, s, []))
