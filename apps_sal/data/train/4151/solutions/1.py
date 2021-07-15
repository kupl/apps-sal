def part(arr):
    terms = {'Partridge', 'PearTree', 'Chat', 'Dan', 'Toblerone', 'Lynn', 'AlphaPapa', 'Nomad'}
    marks = ''.join('!' for x in arr if x in terms)
    return "Mine's a Pint" + marks if marks else "Lynn, I've pierced my foot on a spike!!"
