refer_dict = {'a': 'z', 'b': 'a', 'c': 'b', 'd': 'c', 'e': 'd', 'f': 'e', 'g': 'f', 'h': 'g', 'i': 'h', 'j': 'i', 'k': 'j', 'l': 'k', 'm': 'l', 'n': 'm', 'o': 'n', 'p': 'o', 'q': 'p', 'r': 'q', 's': 'r', 't': 's', 'u': 't', 'v': 'u', 'w': 'v', 'x': 'w', 'y': 'x', 'z': 'y'}
s = str(input())
line = s.split('a')
size = len(line)
flag = True
for it in range(size):
    if line[it] != '':
        temp = str()
        for i in line[it]:
            temp += refer_dict[i]
        line[it] = temp
        flag = False
        break
if flag:
    print(s[:-1] + 'z')
else:
    print('a'.join(line))
