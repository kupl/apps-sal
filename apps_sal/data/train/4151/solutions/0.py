def part(arr):
    l = ["Partridge", "PearTree", "Chat", "Dan", "Toblerone", "Lynn", "AlphaPapa", "Nomad"]
    s = len([i for i in arr if i in l])
    return "Mine's a Pint" + "!" * s if s > 0 else 'Lynn, I\'ve pierced my foot on a spike!!'
