from functools import reduce


def validate_rhythm(meter, score):
    num, den, meter = *meter, int.__truediv__(*meter)
    bars = [[int(d) for d in bar] for bar in score.split("|")]
    prod = den * reduce(int.__mul__, (n for bar in bars for n in bar))
    if not prod & (prod - 1):
        divs = [sum(1 / n for n in bar) for bar in bars]
        if all(div == meter for div in divs[1:-1]):
            if all(div == meter for div in (divs[0], divs[-1])):
                return "Valid rhythm"
            if divs[1:] and divs[0] + divs[-1] == meter:
                return "Valid rhythm with anacrusis"
    return "Invalid rhythm"
