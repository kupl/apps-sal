t = input()
k = t.find('0')
print('1' * (len(t) - 1) if k < 0 else t[: k] + t[k + 1: ])
