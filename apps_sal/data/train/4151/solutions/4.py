from collections import Counter

def part(arr):
    c =  Counter([i in {'Partridge','PearTree','Chat','Dan','Toblerone','Lynn','AlphaPapa','Nomad'} for i in arr])
    return "Mine's a Pint" + c[True] * '!' if True in c else "Lynn, I've pierced my foot on a spike!!" 

