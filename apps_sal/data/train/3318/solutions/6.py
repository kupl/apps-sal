def number_of_carries(a, b):
    a, b = str(a)[::-1], str(b)[::-1]
    l = max(len(a), len(b))
    carry, carries = 0, 0
    for col in [int(m)+int(n) for m, n in zip(f"{a:<0{l}s}", f"{b:<0{l}s}")]:
        carry = (col + carry) > 9
        carries += carry
    return carries
