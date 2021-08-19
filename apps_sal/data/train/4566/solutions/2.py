def counting_valleys(s):
    (level, valleys) = (0, 0)
    for step in s:
        if step == 'U' and level == -1:
            valleys += 1
        level += {'U': 1, 'F': 0, 'D': -1}[step]
    return valleys
