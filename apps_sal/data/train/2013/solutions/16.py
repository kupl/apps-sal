# print("Input the string")
st = input()

if st == 'a':
    print('z')
else:
    apos = st.find('a')
    if apos == -1:
        #  No as in the word at all--shift everything down
        answerlist = []
        for ch in st:
            newch = chr(ord(ch) - 1)
            answerlist.append(newch)
        print(''.join(answerlist))
    elif apos > 0:
        #  Shift everything up to the first a
        answerlist = []
        for i in range(0, apos):
            newch = chr(ord(st[i]) - 1)
            answerlist.append(newch)
        print(''.join(answerlist) + st[apos:])
    else:
        #  The hard case--it starts with an a
        #  Find the first non-a
        pos = 1
        while pos < len(st) and st[pos] == 'a':
            pos += 1
        if pos == len(st):  # All letters are a--must change last letter to z
            print(st[0:len(st) - 1] + 'z')
        else:
            # Change everything from pos to the next a
            nextapos = st.find('a', pos + 1)
            if nextapos == -1:  # No more as--change to the end
                answerlist = []
                for i in range(pos, len(st)):
                    newch = chr(ord(st[i]) - 1)
                    answerlist.append(newch)
                print(st[0:pos] + ''.join(answerlist))
            else:   # Change everything between pos and nextapos
                answerlist = []
                for i in range(pos, nextapos):
                    newch = chr(ord(st[i]) - 1)
                    answerlist.append(newch)
                print(st[0:pos] + ''.join(answerlist) + st[nextapos:])
