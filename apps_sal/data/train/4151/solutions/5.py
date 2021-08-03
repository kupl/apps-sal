related = {"Partridge", "PearTree", "Chat", "Dan", "Toblerone", "Lynn", "AlphaPapa", "Nomad"}


def part(arr):
    found = sum(1 for w in arr if w in related)
    return f"Mine's a Pint{'!' * found}" if found else "Lynn, I've pierced my foot on a spike!!"
