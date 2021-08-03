def parse(crontab):
    crontab = crontab.replace('FEB', '2').replace('JUL', '7').replace('SUN', '0').replace('THU', '4').split()
    output = [[], [], [], [], []]
    valid = {0: [0, 59], 1: [0, 23], 2: [1, 31], 3: [1, 12], 4: [0, 6]}

    def parser(s):
        nums = '1234567890'
        out = []
        dig1 = dig2 = dig3 = ''
        state = 0
        for c in s:
            if c == ',':
                if not(dig3):
                    dig3 = '1'
                out.append([dig1, dig2, dig3])
                dig1 = dig2 = dig3 = ''
                state = 0
            elif not(state):
                dig1 += c
                state = 1
            elif state == 1:
                if c in nums:
                    dig1 += c
                elif c == '-':
                    state = 2
                else:
                    state = 3
            elif state == 2:
                if c in nums:
                    dig2 += c
                else:
                    state = 3
            elif state == 3:
                dig3 += c
        if not(dig3):
            dig3 = '1'
        out.append([dig1, dig2, dig3])
        return out
    for i in range(len(crontab)):
        for p in parser(crontab[i]):
            if p[0] == '*':
                output[i].extend([x for x in range(valid[i][0], valid[i][1] + 1, int(p[2]))])
            elif p[1]:
                output[i].extend([x for x in range(int(p[0]), int(p[1]) + 1, int(p[2])) if valid[i][0] <= x <= valid[i][1]])
            else:
                output[i].append(int(p[0]))
        output[i].sort()
        output[i] = ' '.join([str(x) for x in output[i]])
    return 'minute         ' + output[0] + '\nhour           ' + output[1] + '\nday of month   ' + output[2] + '\nmonth          ' + output[3] + '\nday of week    ' + output[4]
