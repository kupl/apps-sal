check = {"Partridge", "PearTree", "Chat", "Dan", "Toblerone", "Lynn", "AlphaPapa", "Nomad"}.__contains__


def part(arr):
    result = sum(map(check, arr))
    return f"Mine's a Pint{'!'*result}" if result else "Lynn, I've pierced my foot on a spike!!"
