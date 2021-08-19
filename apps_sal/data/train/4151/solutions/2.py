def part(arr):
    terms = frozenset(['Partridge', 'PearTree', 'Chat', 'Dan', 'Toblerone', 'Lynn', 'AlphaPapa', 'Nomad'])
    count = sum((1 for x in arr if x in terms))
    return "Mine's a Pint" + '!' * count if count > 0 else "Lynn, I've pierced my foot on a spike!!"
