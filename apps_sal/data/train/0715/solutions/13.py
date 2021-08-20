s = input()
n = len(s)
v = 0
for i in range(n):
    if s[i] == 'A':
        v += 27
    elif s[i] == 'B':
        v += 26
    elif s[i] == 'C':
        v += 25
    elif s[i] == 'D':
        v += 24
    elif s[i] == 'E':
        v += 23
    elif s[i] == 'F':
        v += 22
    elif s[i] == 'G':
        v += 21
    elif s[i] == 'H':
        v += 20
    elif s[i] == 'I':
        v += 19
    elif s[i] == 'J':
        v += 18
    elif s[i] == 'K':
        v += 17
    elif s[i] == 'L':
        v += 16
    elif s[i] == 'M':
        v += 15
    elif s[i] == 'N':
        v += 14
    elif s[i] == 'O':
        v += 13
    elif s[i] == 'P':
        v += 12
    elif s[i] == 'Q':
        v += 11
    elif s[i] == 'R':
        v += 10
    elif s[i] == 'S':
        v += 9
    elif s[i] == 'T':
        v += 8
    elif s[i] == 'U':
        v += 7
    elif s[i] == 'V':
        v += 6
    elif s[i] == 'W':
        v += 5
    elif s[i] == 'X':
        v += 4
    elif s[i] == 'Y':
        v += 3
    elif s[i] == 'Z':
        v += 2
print(v)
