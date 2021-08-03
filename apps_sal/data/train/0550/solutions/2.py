try:
    def ts(s):
        str1 = ""
        for ele in s:
            str1 += ele
        return str1

    for _ in range(int(input())):
        x, y = [int(x) for x in input().split()]
        x = list(bin(x).replace("0b", ""))
        y = list(bin(y).replace("0b", ""))
        xl = len(x)
        yl = len(y)
        if(xl < yl):
            for __ in range(yl - xl):
                x.insert(0, '0')
        else:
            for __ in range(xl - yl):
                y.insert(0, '0')
        l = len(x)
        xor = -1
        rotations = -1
        for i in range(l):
            temp_xor = int(ts(x), 2) ^ int(ts(y), 2)
            if(temp_xor > xor):
                xor = temp_xor
                rotations = i
            temp = x.pop
            y.insert(0, y.pop())
        print(rotations, xor)

except:
    pass
