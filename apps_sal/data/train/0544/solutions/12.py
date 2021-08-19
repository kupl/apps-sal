def find_string(k):
    f = 'abcdefghijklmnop'
    for i in range(0, len(k)):
        if k[i] == '1':
            f = f[len(f) // 2:]
        elif k[i] == '0':
            f = f[:len(f) // 2]
    return f


t = int(input())
while t:
    o = int(input())
    k = input()
    res = ''
    j = 0
    while j + 3 in range(len(k)):
        res = res + find_string(k[j:j + 4])
        j = j + 4
    print(res)
    t = t - 1
