def average_string(s):
    digits = list("zero,one,two,three,four,five,six,seven,eight,nine".split(","))
    values = [digits.index(w) if w in digits else -1 for w in s.split()]
    return "n/a" if not values or -1 in values else digits[sum(values) // len(values)]
