def convert(n):
    base = 1j
    val = 0
    for c in str(n):
        val*= base
        val += int(c)
    return [val.real , val.imag]

