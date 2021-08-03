def add(a, b):
    out = ""
    carry = 0

    a = a.lstrip("0")
    b = b.lstrip("0")

    max_l = max(len(a), len(b))
    a = a.rjust(max_l, "0")
    b = b.rjust(max_l, "0")

    for i in range(1, max_l + 1):
        s, carry = carry, 0
        s += 1 if a[-i] == "1" else 0
        s += 1 if b[-i] == "1" else 0

        carry = s > 1
        out += "01"[s % 2]

    out += "1" * carry
    return out[::-1] if len(out) > 0 else "0"
