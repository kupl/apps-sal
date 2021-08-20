def part(a):
    s = {'Partridge', 'PearTree', 'Chat', 'Dan', 'Toblerone', 'Lynn', 'AlphaPapa', 'Nomad'}
    n = sum((x in s for x in a))
    return "Mine's a Pint{}".format('!' * n) if n else "Lynn, I've pierced my foot on a spike!!"
