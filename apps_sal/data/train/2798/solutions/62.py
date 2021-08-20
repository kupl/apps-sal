def to_alternating_case(string):
    for char in string:
        'if char.isupper():\n            str_ += char.lower()\n        elif char.islower():\n            str_ += char.upper()\n        elif char == " ":\n            str_ += " "\n        elif string.isdigit():\n            return str(string)\n        '
        a = string.swapcase()
    return a


print(to_alternating_case('cIao'))
