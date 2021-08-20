DCT_TO_IB = {unit: 1.024 ** p for (unit, p) in zip('KMGT', range(1, 5))}


def memorysize_conversion(s):
    toB = s[-2] == 'i'
    (v, u) = s.split()
    unit = (u[0] != 'K' and u[0] or 'k') + u[-1] if toB else u[0].upper() + 'i' + u[-1]
    out = float(v) * DCT_TO_IB[u[0].upper()] ** (toB or -1)
    out = f'{out:.3f}'.rstrip('0')
    return f'{out} {unit}'
