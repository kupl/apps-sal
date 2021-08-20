n = int(input())
s = []
for x in range(n):
    a = input()
    a = ' '.join(a.split()[::-1])
    pun = ".,:;'"
    b = ''
    for i in a:
        if i not in pun:
            b += i
    s.append(b)
n = s[::-1]
for i in n:
    print(i)
