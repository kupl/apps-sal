from sys import stdin, stdout

pwd = stdin.readline().rstrip()
n = int(stdin.readline().rstrip())
words = []
for _ in range(n):
    words.append(stdin.readline().rstrip())
    
if pwd in words:
    print('YES')
else:
    possible1 = False
    possible2 = False
    for word in words:
        if word[0]==pwd[1]:
            possible1=True
        if word[1]==pwd[0]:
            possible2=True
    if possible1 and possible2:
        print('YES')
    else:
        print('NO')

