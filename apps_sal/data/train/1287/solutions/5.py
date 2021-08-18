def val(c):
    if c >= '0' and c <= '9':
        return ord(c) - ord('0')
    else:
        return ord(c) - ord('A') + 10


def toDeci(str, base):
    llen = len(str)
    power = 1
    num = 0

    for i in range(llen - 1, -1, -1):

        if val(str[i]) >= base:
            print('Invalid Number')
            return -1
        num += val(str[i]) * power
        power = power * base
    return num


t = int(input())
for _ in range(t):
    s = input()
    s1 = []

    for i in range(len(s)):
        if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
            s1.append(1)
        else:
            s1.append(0)
    s2 = ''.join([str(elem) for elem in s1])
    print(toDeci(s2, 2))
