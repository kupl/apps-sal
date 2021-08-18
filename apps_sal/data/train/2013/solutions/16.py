st = input()

if st == 'a':
    print('z')
else:
    apos = st.find('a')
    if apos == -1:
        answerlist = []
        for ch in st:
            newch = chr(ord(ch) - 1)
            answerlist.append(newch)
        print(''.join(answerlist))
    elif apos > 0:
        answerlist = []
        for i in range(0, apos):
            newch = chr(ord(st[i]) - 1)
            answerlist.append(newch)
        print(''.join(answerlist) + st[apos:])
    else:
        pos = 1
        while pos < len(st) and st[pos] == 'a':
            pos += 1
        if pos == len(st):
            print(st[0:len(st) - 1] + 'z')
        else:
            nextapos = st.find('a', pos + 1)
            if nextapos == -1:
                answerlist = []
                for i in range(pos, len(st)):
                    newch = chr(ord(st[i]) - 1)
                    answerlist.append(newch)
                print(st[0:pos] + ''.join(answerlist))
            else:
                answerlist = []
                for i in range(pos, nextapos):
                    newch = chr(ord(st[i]) - 1)
                    answerlist.append(newch)
                print(st[0:pos] + ''.join(answerlist) + st[nextapos:])
