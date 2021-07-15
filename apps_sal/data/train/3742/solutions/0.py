from collections import Counter

def modes(data):
    cnts = Counter(data)
    mx, mn = max(cnts.values()), min(cnts.values())
    return sorted([k for k in cnts if cnts[k] == mx and cnts[k] != mn])
