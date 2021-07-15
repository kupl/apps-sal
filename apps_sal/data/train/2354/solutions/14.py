st = input()
arr = []
for _ in range(int(input())):
    arr.append(input())

firf = False
secf = False
flag = True
for sbst in arr:
    if sbst == st:
        print('YES')
        flag = False
        break
    if sbst[1] == st[0]:
        firf = True
    if sbst[0] == st[1]:
        secf = True

    if firf and secf:
        print('YES')
        flag = False
        break

if flag:
    print ('NO')

