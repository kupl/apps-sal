n = input()
a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
j = 0
for i in range(len(n)):
    if n[i] == 'A':
        j = j + 27
    if n[i] == 'B':
        j = j + 26
    if n[i] == 'C':
        j = j + 25
    if n[i] == 'D':
        j = j + 24
    if n[i] == 'E':
        j = j + 23
    if n[i] == 'F':
        j = j + 22
    if n[i] == 'G':
        j = j + 21
    if n[i] == 'H':
        j = j + 20
    if n[i] == 'I':
        j = j + 19
    if n[i] == 'J':
        j = j + 18
    if n[i] == 'K':
        j = j + 17
    if n[i] == 'L':
        j = j + 16
    if n[i] == 'M':
        j = j + 15
    if n[i] == 'N':
        j = j + 14
    if n[i] == 'O':
        j = j + 13
    if n[i] == 'P':
        j = j + 12
    if n[i] == 'Q':
        j = j + 11
    if n[i] == 'R':
        j = j + 10
    if n[i] == 'S':
        j = j + 9
    if n[i] == 'T':
        j = j + 8
    if n[i] == 'U':
        j = j + 7
    if n[i] == 'V':
        j = j + 6
    if n[i] == 'W':
        j = j + 5
    if n[i] == 'X':
        j = j + 4
    if n[i] == 'Y':
        j = j + 3
    if n[i] == 'Z':
        j = j + 2
print(j)
