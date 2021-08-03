

vow = ['a', 'e', 'i', 'o', 'u']
for _ in range(int(input())):
    name = str(input())
    tmp = ''
    for i in range(len(name)):
        if name[i] not in vow and name[i].isalpha():
            tmp += '1'
        elif name[i] in vow and name[i].isalpha():
            tmp += '0'

    print(int(tmp, 2) % (10**9 + 7))
