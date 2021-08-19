from sys import stdin

#stdin = open('input.txt')

n = int(stdin.readline())

seq = stdin.readline().split()
carry = seq[0]
result = [carry]

mark = False
cur_len = 0
max_len = 0

i = 1
while i < len(seq) - 1:
    if mark:
        if seq[i] != seq[i + 1]:
            cur_len += 1
        else:
            if cur_len > max_len:
                max_len = cur_len

            if seq[i] == carry:
                result.extend([carry] * cur_len)
            else:
                result.extend([carry] * (cur_len // 2))
                result.extend([seq[i]] * (cur_len // 2))

            result.append(seq[i])
            mark = False
            cur_len = 0
    elif seq[i] != seq[i - 1] and seq[i] != seq[i + 1]:
        mark = True
        cur_len = 1
        carry = seq[i - 1]
    else:
        result.append(seq[i])

    i += 1

if mark:
    if cur_len > max_len:
        max_len = cur_len

    if seq[i] == carry:
        result.extend([carry] * cur_len)
    else:
        result.extend([carry] * (cur_len // 2))
        result.extend([seq[i]] * (cur_len // 2))

result.append(seq[i])

print((max_len + 1) // 2)
for x in result:
    print(x, end=' ')
