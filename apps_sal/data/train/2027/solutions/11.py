n = input()
length = len(n)
(min, max, arr1, arr2) = (1, length, [], [])
for i in range(0, length):
    if n[i] == 'l':
        arr2.append(i + 1)
    else:
        arr1.append(i + 1)
print('\n'.join(map(str, arr1)))
print('\n'.join(map(str, arr2[::-1])))
