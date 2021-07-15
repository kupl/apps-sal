def invert(lst):
    if not lst: return []
    final = []
    i = 0
    while i < len(lst):
      final.append(-lst[i])
      i+=1
    return final
