letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
dataIn = str(input())
data = []
for i in dataIn:
    data.append(i)
count = 0
begin = 0
if len(data) == 1:
    if data[0] == 'a':
        data[0] = 'z'
    else:
        for j in range(len(letters)):
            if letters[j] == data[0]:
                data[0] = letters[j - 1]
else:
    i = 0
    begin = False
    while i < len(data) - 1:
        if data[i] == 'a':
            i += 1
        else:
            break
    for k in range(i, len(data)):
        if data[k] == 'a' and k != len(data) - 1:
            break
        elif data[k] == 'a' and k == len(data) - 1:
            if not begin:
                data[k] = 'z'
        else:
            begin = True
            for j in range(len(letters)):
                if letters[j] == data[k]:
                    data[k] = letters[j - 1]
result = ''
for i in data:
    result += i
print(result)
