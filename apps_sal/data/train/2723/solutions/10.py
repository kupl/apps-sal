digit_map = {
    "zero": 0,
    "nine": 9,
    "five": 5,
    "two": 2,
    "three": 3,
    "four": 4,
    "one": 1,
    "eight": 8,
    "six": 6,
    "seven": 7
}

reverse_digit_map = dict(map(reversed, digit_map.items()))

class InValidNumException(Exception):
    pass

class StringNum(int):
    def __new__(cls, s):
        if s in digit_map:
            return int.__new__(cls, digit_map[s])

        raise InValidNumException()

def average_string(s):
    try:
        arr = [StringNum(t) for t in s.split() if t]

        if len(arr) == 0:
            return 'n/a'

        average = int(sum(arr) / len(arr))
    except InValidNumException:
        return 'n/a'

    if 0 <= average < 10:
        return reverse_digit_map[average]
    return 'n/a'
