n = input()
s = 0
freq = {}
freq['A'] = 27
freq['B'] = 26
freq['C'] = 25
freq['D'] = 24
freq['E'] = 23
freq['F'] = 22
freq['G'] = 21
freq['H'] = 20
freq['I'] = 19
freq['J'] = 18
freq['K'] = 17
freq['L'] = 16
freq['M'] = 15
freq['N'] = 14
freq['O'] = 13
freq['P'] = 12
freq['Q'] = 11
freq['R'] = 10
freq['S'] = 9
freq['T'] = 8
freq['U'] = 7
freq['V'] = 6
freq['W'] = 5
freq['X'] = 4
freq['Y'] = 3
freq['Z'] = 2
for i in n:
    if i in freq:
        s = s + freq[i]
print(s)
