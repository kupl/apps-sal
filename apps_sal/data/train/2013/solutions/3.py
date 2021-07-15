st = input()
st1 = ""
others = False
length = len(st)
for i in range(0, length):
    if i == length - 1 and others is False:
        st1 += str(chr(((ord(st[i]) - 98) % 26) + 97))
        break
    if st[i] == 'a':
        if others is True:
            st1 += st[i:length]
            break
        st1 += str(st[i])
    else:
        others = True
        st1 += str(chr(ord(st[i]) - 1))
print(st1)

