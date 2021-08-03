from sys import stdin

#stdin = open('input.txt')

n = int(stdin.readline())

seq = stdin.readline().split()
result = [0] * n
result[0] = seq[0]

mark = False
cur_len = 0
max_len = 0
carry = 0
carry_id = 0

i = 1
while i < len(seq) - 1:
    if mark:
        if seq[i] != seq[i + 1]:
            cur_len += 1
        else:
            if cur_len > max_len:
                max_len = cur_len

            if seq[i] == carry:
                # result.extend([carry]*cur_len)
                result[carry_id: i: 1] = [carry] * cur_len
            else:
                # result.extend([carry]*(cur_len//2))
                # result.extend([seq[i]]*(cur_len//2))
                result[carry_id: carry_id + cur_len // 2: 1] = [carry] * (cur_len // 2)
                result[carry_id + cur_len // 2: i: 1] = [seq[i]] * (cur_len // 2)

            result[i] = seq[i]
            mark = False
            cur_len = 0
    elif seq[i] != seq[i - 1] and seq[i] != seq[i + 1]:
        mark = True
        cur_len = 1
        carry = seq[i - 1]
        carry_id = i
    else:
        result[i] = seq[i]

    i += 1

if mark:
    if cur_len > max_len:
        max_len = cur_len

    if seq[i] == carry:
        # result.extend([carry]*cur_len)
        result[carry_id: i] = [carry] * cur_len
    else:
        # result.extend([carry]*(cur_len//2))
        # result.extend([seq[i]]*(cur_len//2))
        result[carry_id: carry_id + cur_len // 2] = [carry] * (cur_len // 2)
        result[carry_id + cur_len // 2: i] = [seq[i]] * (cur_len // 2)

result[i] = seq[i]

print((max_len + 1) // 2)
for x in result:
    print(x, end=' ')
