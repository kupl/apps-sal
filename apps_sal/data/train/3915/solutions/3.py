def solve(input_string):
    res = []
    for i in input_string.split("\n"):
        res.append(carry(i.split()[0], i.split()[1]))
    return "\n".join(res)


def carry(s1, s2):
    carry = 0
    increment = 0
    for i, j in zip(s1[::-1], s2[::-1]):
        digit = int(i) + int(j) + increment
        increment = 1 if digit >= 10 else 0
        carry += increment
    return "No carry operation" if not carry else f"{carry} carry operations"
