def dec(n):
    return bin(n).replace('0b', '')


def ss(str):
    if len(str) <= 1:
        return str
    mid = str[1:len(str)]
    return mid + str[0]


def btd(q):
    q1 = q
    (decimal, i, n) = (0, 0, 0)
    while q != 0:
        dec = q % 10
        decimal = decimal + dec * 2 ** i
        q = q // 10
        i += 1
    return decimal


t = int(input())
for iw in range(0, t):
    a = input()
    arr = []
    we = []
    x = a.split()
    string = str(dec(int(x[1])))
    string2 = str(dec(int(x[0])))
    d = int(x[0])
    if len(string) > len(string2):
        l = len(string)
    else:
        l = len(string2)
        for lk in range(0, len(string2) - len(string)):
            string = '0' + string
    for k in range(0, l):
        c = int(x[1])
        arr.append(d ^ c)
        string = ss(string)
        x[1] = btd(int(string))
    for h in range(0, len(arr)):
        if max(arr) == arr[h]:
            if h == 0:
                we.append(0)
                break
            else:
                we.append(len(arr) - h)
    print(min(we), max(arr))
