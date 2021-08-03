inp = input()
length = len(inp)
min, max, dic1, dic2 = 1, length, [], []
for i in range(0, length):
    if inp[i] == "l":
        dic2.append(i + 1)
    else:
        dic1.append(i + 1)

print('\n'.join(map(str, dic1)))
print('\n'.join(map(str, dic2[::-1])))
