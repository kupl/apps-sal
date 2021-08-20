def isVowel(char):
    return char in 'aeiou'


n = int(input())
for _ in range(n):
    s = input()
    p = 0
    q = 0
    for i in s:
        if isVowel(i):
            p = p + 1
        elif i > 'a' and i < 'e':
            if i == 'c':
                q = q + 2
            else:
                q = q + 1
        elif i > 'e' and i < 'i':
            if i == 'g':
                q = q + 2
            else:
                q = q + 1
        elif i > 'i' and i < 'o':
            if i == 'l':
                q = q + 3
            elif i == 'k' or i == 'm':
                q = q + 2
            else:
                q = q + 1
        elif i > 'o' and i < 'u':
            if i == 'r':
                q = q + 3
            elif i == 'q' or i == 's':
                q = q + 2
            else:
                q = q + 1
        elif i > 'u':
            if i == 'x':
                q = q + 3
            elif i == 'y':
                q = q + 4
            elif i == 'z':
                q = q + 5
            elif i == 'w':
                q = q + 2
            else:
                q = q + 1
        else:
            p = p + 1
    print(q)
