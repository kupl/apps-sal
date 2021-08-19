S = {'Partridge', 'PearTree', 'Chat', 'Dan', 'Toblerone', 'Lynn', 'AlphaPapa', 'Nomad'}


def part(arr):
    n = sum((w in S for w in arr))
    return "Lynn, I've pierced my foot on a spike!!" if not n else "Mine's a Pint" + '!' * n
