def scanner(qrcode):
    result = ''
    dict = {1: 0, 0: 1}
    (x, y) = (20, 20)
    bool = True
    dir = 'Up'
    i = 2
    count = 0
    while count < 6:
        while x > 8 and dir == 'Up':
            if (x + y) % 2 == 0:
                result += str(dict[qrcode[x][y]])
            else:
                result += str(qrcode[x][y])
            if bool:
                y -= 1
                bool = False
            else:
                x -= 1
                y += 1
                bool = True
            if x == 8:
                x = 9
                y = 20 - i
                i += 2
                dir = 'Down'
                bool = True
        print(result)
        count += 1
        if count == 5:
            break
        else:
            while x < 21 and dir == 'Down':
                if (x + y) % 2 == 0:
                    result += str(dict[qrcode[x][y]])
                else:
                    result += str(qrcode[x][y])
                if bool:
                    y -= 1
                    bool = False
                else:
                    x += 1
                    y += 1
                    bool = True
                if x == 21:
                    x = 20
                    y = 20 - i
                    i += 2
                    dir = 'Up'
                    bool = True
            count += 1
            print(result)
    len = int(result[4:12], 2)
    ans = ''
    for i in range(len):
        ans += chr(int(result[12 + i * 8:20 + i * 8], 2))
    return ans
