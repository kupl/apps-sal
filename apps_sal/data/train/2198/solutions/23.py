def check(result, s, i):
    while True:
        if s == result[i]:
            return True
        else:
            if s.count('h') > 0 and result[i].count('kh') > 0 and len(s) < len(result[i]):
                s.replace('h', 'kh')
            elif s.count('kh') > 0 and result[i].count('h') > 0 and len(s) > len(result[i]):
                result[i].replace('h', 'kh')
            else:
                return False


n = int(input(''))

s = list()

for _ in range(n):
    temp = input('').replace('u', 'oo')
    while temp.count('kh') > 0:
        temp = temp.replace('kh', 'h')
    s.append(temp)

result = list()

for temp in s:
    flag = False
    for i in result:
        if temp == i:
            flag = True
            break
    if not flag:
        result.append(temp)

print(len(result))
