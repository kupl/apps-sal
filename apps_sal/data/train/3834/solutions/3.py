def palin(a,b):
    res = int('1' + ('0' * (a-1))) + 1
    q = a//2
    step = ('1' + (q*'0'), '11'+ ((q-1)*'0'))[a%2==0]
    l = []
    while b>0:
        temp = len(str(res))//2
        res = str(res)
        res = res[:-temp] + res[:temp][::-1]
        if len(res) > a:
            a = len(str(res))
            q = a // 2
            step = ('1' + (q * '0'), '11' + ((q - 1) * '0'))[a % 2 == 0]
        if l and l[-1] == 99:
            l.append(101)
        if res == res[::-1]:
            b-=1
            l.append(int(res))
        res = int(res)
        if str(res + int(step))[:temp-1] != str(res)[:temp-1]:
            temp_res = int(str(res)) + 1
            while str(temp_res) != str(temp_res)[::-1]:
                temp_res += 1
            b -= 1
            if b >= 0:
                l.append(temp_res)
        res += int(step)
    return l[-1]
