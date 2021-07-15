def skrzat(base, number):
    convertor = { "b": {"name": "binary", "func": from_weird_binary},
          "d": {"name": "decimal", "func": to_weird_binary} }
    return "From {}: {} is {}".format(convertor[base]["name"], number, convertor[base]["func"](number))

def to_weird_binary(number):
    res = ""
    while number:
        number, x = divmod(number, -2)
        if x < 0:
            number += 1
        res += str(abs(x))
    return res[::-1] or "0"

def from_weird_binary(number):
    return sum([int(d) * (-2) ** i for i, d in enumerate(reversed(number))])
