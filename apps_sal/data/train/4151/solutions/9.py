def part(arr):
    st = frozenset(('Partridge', 'PearTree', 'Chat', 'Dan', 'Toblerone', 'Lynn', 'AlphaPapa', 'Nomad'))
    s = sum(x in st for x in arr)
    return "Mine's a Pint" + '!' * s if s else "Lynn, I've pierced my foot on a spike!!"
