from fractions import Fraction


VALID_CHARS = {"1", "2", "4", "8"}


def note_sum(s):
    return sum(Fraction(1, x) for x in map(int, s))


def validate_rhythm(meter, score):
    if meter[1] not in [1, 2, 4, 8]:
        return "Invalid rhythm"
    ss = score.split("|")
    if not all(s and all(x in VALID_CHARS for x in s) for s in ss):
        return "Invalid rhythm"

    note = Fraction(*meter)
    if all(note_sum(s) == note for s in ss):
        return "Valid rhythm"
    ss[0] += ss.pop()
    if all(note_sum(s) == note for s in ss):
        return "Valid rhythm with anacrusis"
    return "Invalid rhythm"
